import polars as pl
from polars import DataFrame

from metadata.dd.DdActif import CdClasseActif, VarActif
from metadata.dd.DdAlm import StratAlmCas, VarAlm
from metadata.dd.DdCommun import VarCommun
from metadata.dd.DdFgx import VarFgx
from metadata.dd.DdPassifEp import VarPassif
from metadata.dd.DdProjection import VarProj
from metadata.dd.DdS2 import VarS2
from metadata.dd.DdStratInv import VarStratInv
from metadata.dfmd.DfMdCommun import DfMdCommun
from metadata.dfmd.DfMdActif import DfMdActif
from metadata.dfmd.DfMdAlmCr import DfMdAlm, stratAlmCasOrdrePriorite
from metadata.dfmd.DfMdPassifEp import DfMdPassif
from metadata.dfmd.DfMdProj import DfMdProj

def almCrAlmOutputPassifFromTxServiBrt(almCrInputPassif:DataFrame, almCrInputTxServiBrt:DataFrame, colTxServiBrt:str) -> DataFrame:

    """Méthode en charge d'appliquer les taux servis aux contrats afin de calculer les PB par contra
    :param almCrInputPassif: DataFrame contenant les inputs de la stratégie ALM par contrat (txIc, taf, mtPbAss notamment)
    :type almCrInputPassif: DataFrame
    :param almCrInputTxServi: Dataframe contenant notamment les cibles de taux servis dans les 3 cas "TX_SERVI_CIBLE", "TX_SERVI_CIBLE_DIV2", "TMG"
    :type almCrInputTxServi: DataFrame
    :return: DataFrame almCrAlmOutputPassif contenant notamment les variables suivantes mtPbBrt, mtCsg, mtPbNet par contrat
    :rtype: DataFrame
    """

    almCrInputTxServiBrt = almCrInputTxServiBrt.rename({colTxServiBrt : VarAlm.txServiBrt})

    almCrAlmOutputPassif = almCrInputPassif.join(
        almCrInputTxServiBrt,
        how='left',
        on=set(almCrInputPassif.columns) & set(almCrInputTxServiBrt.columns)
    ).with_columns([
        pl.max_horizontal(pl.col(VarPassif.taf) * pl.col(VarAlm.txServiBrt) - pl.col(VarPassif.tfgse),pl.col(VarPassif.txIc)).alias(VarAlm.txServiNet),
    ]).with_columns([
        pl.max_horizontal(pl.col(VarPassif.mtPbAss) * pl.col(VarAlm.txServiBrt), pl.col(VarPassif.mtIcSort) + pl.col(VarPassif.mtIcRest)).alias(VarActif.mtPfi),
        (pl.col(VarPassif.mtPbAss) * pl.col(VarAlm.txServiNet) - pl.col(VarPassif.mtIcRest)).alias(VarPassif.mtPbBrt),
    ]).with_columns(
        pl.lit(0.0).alias(VarPassif.mtCsg)
    ).with_columns(
        ( pl.col(VarPassif.mtPbBrt) - pl.col(VarPassif.mtCsg) ).alias(VarPassif.mtPbNet)
    )

    return almCrAlmOutputPassif

def almCrAlmOutputPassifFromMtPfi(almCrInputPassif:DataFrame, almCrInputMtPfi:DataFrame, colMtPfi:str) -> DataFrame:

    almCrAlmOutputPassif = almCrAlmOutputPassif.sort(
        [VarS2.cdChocS2, *DfMdProj().mdPksScPer, *DfMdCommun().mdPksCanton, VarAlm.stratAlmCas, VarPassif.txIcBrt]
    ).with_columns(
        pl.col(VarPassif.mtIcRest).cumsum().over(
            [VarS2.cdChocS2, *DfMdProj().mdPksScPer, *DfMdCommun().mdPksCanton, VarAlm.stratAlmCas]
        ).alias(VarPassif.mtIcRest + "_cumsum")
    )

    return almCrAlmOutputPassif

def buildAlmCrInputActif(projActifPerfT:DataFrame, 
                         projActifStratInvT:DataFrame,
                         projProvOther:DataFrame,
                         hypStratInvTxFraisPlct:DataFrame,
                         hypStratAlmCr:DataFrame) -> DataFrame:

    """Méthode en charge de la construction de l'input de la stratégie ALM pour les actifs

    :param projActifPerfT: DataFrame projActif post Performance
    :type projActifPerfT: DataFrame
    :param projActifStratInvT: DataFrame projActif post Stratégie d'investissement
    :type projActifStratInvT: DataFrame
    :param projProvOther: Etat courant des provisions projetés
    :type projProvOther: DataFrame
    :param hypStratInvTxFraisPlct: DataFrame issu de l'input ACAP contenant notamment les taux de frais de placement
    :type hypStratInvTxFraisPlct: DataFrame
    :return: DataFrame almCrInputActif

    Ceci est réalisé via les actions suivantes :

    * Il est possible de calculer la Vc Moyenne de l'année en

        * agrégeant mtVcAv du DataFrame projActifPerfT par canton
        * agrégeant mtVc du DataFrame projActifStratInvT par canton
        * en faisant la différence entre les deux

    * Pour le calcul des PMVl disponibles

        * On agrège les PMVL présentes dans le DataFrame projActifStratInvT et on exclut les PMVL des obligations
        * Si on est dans le cas du BEG, pas de PMVL disponibles pour l'ALM

    * mtFgxPlct est calculé sur la base de mtVm du DataFrame projActifStratInvT

    * les produits financiers mtPfi correspondent

        * A la somme des produits financiers issus de la performance et de la stratégie d'investissement
        * A laquelle on retranche le delta de RC

    """

    mdAlmCrInputActif = dfMdAlmCr.mdAlmCrInputActif

    almCrInputActifPmvl = projActifStratInvT.select(
        [*dfMdActif.mdProjActif.pks, VarActif.mtPmvl]
    ).with_columns(
        pl.when(pl.col(VarActif.cdClasseActif) == CdClasseActif.OBLIGATION)
        .then(pl.lit(0.0))
        .otherwise(pl.col(VarActif.mtPmvl))
        .alias(VarActif.mtPmvl)
    ).drop(VarProj.evenement).group_by(mdAlmCrInputActif.pks).sum()
    
    almCrInputActifFgxPlct = projActifStratInvT.join(
        hypStratInvTxFraisPlct, 
        how='left',
        on=dfMdActif.mdHypStratInvTxFraisPlct.pks
    ).with_columns(
        (pl.col(VarActif.mtVm) * pl.col(VarStratInv.txFraisPlct)).clip_min(0.0).alias(VarFgx.mtFgxPlct)
    ).select(
        [*dfMdActif.mdProjActif.pks, VarActif.mtVc, VarActif.mtVm, VarFgx.mtFgxPlct]
    ).drop(VarProj.evenement).group_by(mdAlmCrInputActif.pks).sum()

    almCrInputActifPfiRC = projProvOther.with_columns(
        (pl.col(VarAlm.mtReserveCapiAv) - pl.col(VarAlm.mtReserveCapi)).alias(VarActif.mtPfi)
    ).select(
        [*dfMdAlmCr.mdProjProvOther.pks, VarActif.mtPfi]
    ).drop(VarProj.evenement).group_by(mdAlmCrInputActif.pks).sum() \
    .select([*mdAlmCrInputActif.pks, VarActif.mtPfi])

    # On somme les pfis de l'année
    almCrInputActifPfiActifs = pl.concat([
        projActifPerfT.select([*mdAlmCrInputActif.pks, VarActif.mtPfi]), 
        projActifStratInvT.select([*mdAlmCrInputActif.pks, VarActif.mtPfi])
    ]).drop(VarProj.evenement).group_by(mdAlmCrInputActif.pks).sum() \
    

    almCrInputActifPfi = pl.concat([almCrInputActifPfiRC, almCrInputActifPfiActifs]).group_by(mdAlmCrInputActif.pks).sum()

    # On agrège tout
    almCrInputActif = almCrInputActifPfi.join(
        almCrInputActifFgxPlct,
        how='left',
        on=dfMdAlmCr.mdAlmCrInputActif.pks
    ).join(
        almCrInputActifPmvl,
        how='left',
        on=dfMdAlmCr.mdAlmCrInputActif.pks
    ).join(
        hypStratAlmCr,
        how='left',
        on=dfMdAlmCr.mdHypStratAlmCr.pks
    ).with_columns(
        pl.lit(1.0).alias(VarAlm.txPfiAsseRepartPc)
    ).rename({VarActif.mtPfi : VarAlm.mtPfiInit})

    return almCrInputActif.select(dfMdAlmCr.mdAlmCrInputActif.allColumns)

def buildAlmCrInputTxServiCible(almCrInputActif:DataFrame, hypStratAlmTxServi:DataFrame, gseOutputObligPzcT:DataFrame):

    """Méthode déterminant le taux à servir par canton en fonction des hypothèses pertinentes

    :param chocS2: Choc Solvabilité 2
    :type chocS2: str
    :param iteration: Itération
    :type iteration: int
    :param gseOutputObligPzcT: Prix zéro coupon des obligations à t
    :type gseOutputObligPzcT: DataFrame
    :param hypStratAlmTxServi: Paramétrage du taux servi
    :type hypStratAlmTxServi: DataFrame
    :return: DataFrame almCrInputTxServiCible contenant les taux servis cible par canton et stratAlmCas
    :rtype: DataFrame

    A date, la définition des taux cibles n'est pas dynamique et est réalisé via la lecture simple de la table SPBP en entrée.
    """
    almCrInputTxServiCible = almCrInputActif.select(dfMdAlmCr.mdAlmCrInputActif.pks) \
        .join(
            hypStratAlmTxServi,
            how='left',
            on=dfMdAlmCr.mdHypStratAlmTxServi.pks
        ).join(
            stratAlmCasOrdrePriorite,
            how='cross',
        ).with_columns(
            pl.when(pl.col(VarAlm.stratAlmCas) == StratAlmCas.TX_CIBLE)
            .then(pl.col(VarAlm.txCibleFixe))
            .when(pl.col(VarAlm.stratAlmCas) == StratAlmCas.TX_CIBLE_DIV2)
            .then(pl.col(VarAlm.txCibleFixe) / 2.0)
            .otherwise(0.0)
            .alias(VarAlm.txCible)
        )

    return almCrInputTxServiCible