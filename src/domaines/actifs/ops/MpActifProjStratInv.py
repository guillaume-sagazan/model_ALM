import logging
from datetime import date, datetime

import polars as pl
from polars import DataFrame



from config.ErrConfig import OnErrorStrategy
# from domaines.actif.pipelines.MpActifsOblig import mpActifObligInitCalcTra, mpActifObligInitVmRn
# from domaines.actif.pipelines.ProjActifOblig import projActifObligBuild, projActifObligCfBuild
from domaines.actifs.expr.ActifsExpr import calcPmvl
# from domaines.provisions.pipelines.ProjProvOther import projProvOtherCopy
# from domaines.provisions.pipelines.ProjProvPpe import projProvPpeCopy
from domaines.actifs.ops.MpActifProjCopy import mpActifProjCopy
from metadata.dd.DdAlm import VarAlm
from metadata.dd.DdS2 import VarS2
from metadata.dd.DdStratInv import VarStratInv
from metadata.dd.DdActif import VarActif
from metadata.dd.DdCommun import VarCommun, VarCommun
from metadata.dd.DdActif import CdClasseActif
from metadata.dd.DdProjection import ModeleAlmEvenement, VarProj
from metadata.dfmd.DfMdActif import dfMdActif
# from metadata.dfmd.DfMdAlmCr import DfMdAlm
from metadata.dfmd.DfMdCommun import dfMdCommun
from metadata.dfmd.DfMdProj import dfMdProj


def projActifObligStratInvApplyAchatOblig(period : int, projAnnee : int,
                                       projActifObligMp : DataFrame, projActifObligCf : DataFrame, projActifOblig : DataFrame,
                                       invStratInputOutputAchatOblig : DataFrame, hypStratInvObligAchat:DataFrame,
                                       gseOutputObligPzcT:DataFrame, gseObligMaturiteMax:int,
                                       errorZero:float, errorZeroRelatif:float,
                                       initActifObligTraIterMax:int,
                                       initActifErrorStrategy:OnErrorStrategy,
                                       onErrorStrategy:OnErrorStrategy
                                       ):
    """Méthode en charge de l'achat de titres obligataires lors de la stratégie d'investissement

    :param chocS2:
    :type chocS2:
    :param period:
    :type period:
    :param projAnnee:
    :type projAnnee:
    :param mpActifOblig:
    :type mpActifOblig:
    :param projActifObligCf:
    :type projActifObligCf:
    :param projActifOblig:
    :type projActifOblig:
    :param invStratInputOutputAchatOblig:
    :type invStratInputOutputAchatOblig:
    :param hypStratInvObligAchat:
    :type hypStratInvObligAchat:
    :param gseOutputObligPzcT:
    :type gseOutputObligPzcT:
    :param gseObligMaturiteMax:
    :type gseObligMaturiteMax:
    :param errorZero:
    :type errorZero:
    :param errorZeroRelatif:
    :type errorZeroRelatif:
    :param initActifObligTraIterMax:
    :type initActifObligTraIterMax:
    :param initActifErrorStrategy:
    :type initActifErrorStrategy:
    :param onErrorStrategy:
    :type onErrorStrategy:
    :return:
    :rtype:
    """
    projActifObligMpAchat = invStratInputOutputAchatOblig.filter(
        (pl.col(VarStratInv.mtAchatOblig) > 0) & (pl.col((VarActif.cdClasseActif)) == CdClasseActif.OBLIGATION)
    ).join(
        hypStratInvObligAchat,
        how='left',
        on=dfMdActif.mdHypStratInvObligAchat.pks
    ).rename({VarStratInv.txObligAchatCpn: VarActif.txCpn}) \
    .with_columns([
        pl.lit('projection').alias(VarProj.cdTrajectoire),
        pl.lit(date(projAnnee, 12, 31)).alias(VarProj.dtTrajectoire),
        pl.lit('OBLIG' + str(period)).alias(VarActif.cdIsin),
        pl.lit(date(projAnnee, 12, 31)).alias(VarCommun.dtDateTerme),
        (pl.lit(projAnnee) + pl.col(VarStratInv.nbObligAchatMaturite)).cast(pl.Int32).alias(VarCommun.dtDateTermeAnnee),
        (pl.lit(period) + pl.col(VarStratInv.nbObligAchatMaturite)).cast(pl.Int32).alias(VarActif.nbPeriodTerme),
        pl.lit(1.0).alias(VarActif.mtNominal),
        pl.lit(1.0).alias(VarActif.txRemboursement),
        pl.col(VarStratInv.mtAchatOblig).alias(VarActif.mtVm),
        pl.col(VarStratInv.mtAchatOblig).alias(VarActif.mtVc),
        pl.col(VarStratInv.mtAchatOblig).alias(VarActif.mtVcTra),
        pl.lit(0.0).cast(pl.Float64).alias(VarActif.nbDuration),
        pl.lit(7).cast(pl.Int32).alias(VarActif.cdCqs),
        pl.col(VarActif.txCpn).alias(VarActif.txTra)
    ])

    projActifObligAchatCf = projActifObligCfBuild(period=period, mpActifOblig=projActifObligMpAchat)

    projActifObligMpAchat, projActifObligAchatCf, mpActifObligErreursAchat = mpActifObligInitVmRn(
        mpActifOblig=projActifObligMpAchat,
        projActifObligCf=projActifObligAchatCf,
        gseCtRefObligPzc=gseOutputObligPzcT,
        errorZeroRelatif=errorZeroRelatif
    )
    projActifObligMpAchat, projActifObligAchatCf, mpActifObligErreursAchat = mpActifObligInitCalcTra(
        mpActifOblig=projActifObligMpAchat,
        projActifObligCf=projActifObligAchatCf,
        errorZeroRelatif=errorZeroRelatif,
        initActifObligTraIterMax=initActifObligTraIterMax
    )
    
    projActifObligMpAchat = projActifObligMpAchat.select(dfMdActif.mdProjActifObligMp.allColumns)

    projActifObligAchat = projActifObligBuild(period=period, evenement=ModeleAlmEvenement.StratInv, mpActifOblig=projActifObligMpAchat, projActifObligCf=projActifObligAchatCf, gseOutputObligPzcT=gseOutputObligPzcT)
    
    projActifObligAchat = projActifObligAchat.with_columns(
            (-1.0 * pl.col(VarActif.mtVm)).alias(VarActif.mtCf)
        ).select(dfMdActif.mdProjActif.allColumns)

    projActifObligMp = pl.concat([projActifObligMp, projActifObligMpAchat])
    projActifObligCf = pl.concat([projActifObligCf, projActifObligAchatCf])
    projActifOblig = pl.concat([projActifOblig, projActifObligAchat])

    return projActifObligMp, projActifObligCf, projActifOblig, None



def projProvOtherStratInv(period:int, projProvOther : DataFrame, projActifOblig : DataFrame) -> DataFrame: # TODO : A deplacer

    """Méthode en charge d'appliquer la stratégie d'investissement sur les provisions comptables

    :param period: Iteration
    :type period: int
    :param projProvOther: DataFrame projProvOther en input
    :type projProvOther: DataFrame
    :param projActifOblig: Titres obligataires
    :type projActifOblig: DataFrame

    :return: DataFrame projProvOther mis à jour
    :rtype: DataFrame

    """

    projProvOther = projProvOtherCopy(period=period, projProvOther=projProvOther,
                          evenement=ModeleAlmEvenement.StratInv)
    return projProvOther

def projProvPpeStratInv(period:int, projProvPpe: DataFrame) -> DataFrame: # TODO : A deplacer

    """Méthode en charge d'appliquer la stratégie d'investissement

    :param period: Itération
    :type period: int
    :param projProvPpe: Générations de PPB
    :type projProvPpe: DataFrame
    :return: DataFrame ProjProvPpe mis à jour
    :rtype: DataFrame
    """

    projProvPpe = projProvPpeCopy(projProvPpe=projProvPpe, period=period,
                        evenement=ModeleAlmEvenement.StratInv)
    return projProvPpe


def projActifObligCfStraInvApplyAchatVente(projActifObligCf : DataFrame, stratInvInputOutput : DataFrame) -> DataFrame:
    """Méthode en charge d'impacter les cashflows futurs des titres obligataires du facteur d'achat vente
    :param projActifObligCf:
    :type projActifObligCf: DataFrame
    :param projActifOblig:
    :type projActifOblig: DataFrame
    :return:
    :rtype: DataFrame
    """

    projActifObligCf = projActifObligCf.join(
        stratInvInputOutput.select([*dfMdActif.mdStratInvInputOutput.pks, VarStratInv.facteurAchatVente]),
        how='left',
        on=dfMdActif.mdStratInvInputOutput.pks
    ).with_columns(
        pl.when(pl.col(VarStratInv.facteurAchatVente) < 1.0)
        .then(pl.col(VarActif.mtCf) * pl.col(VarStratInv.facteurAchatVente))
        .otherwise(pl.col(VarActif.mtCf))
        .alias(VarActif.mtCf)
    )

    return projActifObligCf.select(dfMdActif.mdProjActifObligCf.allColumns)



def mpActifProjStratInvApplyFacteurAchatVente(period : int,mpActifProj : DataFrame, stratInvInputOutput : DataFrame) -> DataFrame:
    """Méthode en charge d'appliquer les achats ventes (hors achats d'obligations) sur les actifs unitaires
    :param projActif: Portefeuille d'actifs sur lequel appliquer les achats ventes
    :type projActif: DataFrame
    :param stratInvInputOutput: DataFrame contenant les intermédiaires de calcul et les outputs de la stratégie d'investissement
    :type stratInvInputOutput: DataFrame
    :return: DataFrame projActif mis à jour
    :rtype: DataFrame
    """
    
    mdStratInvInputOutput = dfMdActif.mdStratInvInputOutput

    rsVente : pl.Expr = pl.col(VarStratInv.facteurAchatVente) <= 1.
    rsAchat = (pl.col(VarStratInv.facteurAchatVente) > 1.) & (pl.col(VarActif.cdClasseActif) != CdClasseActif.OBLIGATION)
    rsCash = pl.col(VarActif.cdClasseActif) == CdClasseActif.MONETAIRE

    mpActifProj =mpActifProjCopy(mpActifProj = mpActifProj,evenement=ModeleAlmEvenement.StratInv,period=period).join(
       stratInvInputOutput.select([*mdStratInvInputOutput.pks, VarStratInv.facteurAchatVente]),
       how='left',
       on=mdStratInvInputOutput.pks     
    ).with_columns([
        pl.when(rsVente)
        .then(pl.col(VarActif.mtVmAv) * pl.col(VarStratInv.facteurAchatVente))
        .otherwise(pl.col(VarActif.mtVm))
        .alias(VarActif.mtVm),
        pl.when(rsVente)
        .then(pl.col(VarActif.mtVcAv) * pl.col(VarStratInv.facteurAchatVente))
        .otherwise(pl.col(VarActif.mtVc))
        .alias(VarActif.mtVc),
        pl.when(rsVente)
        .then((pl.col(VarActif.mtVmAv) - pl.col(VarActif.mtVcAv)) * (1.0 - pl.col(VarStratInv.facteurAchatVente)))
        .otherwise(pl.col(VarActif.mtPfi))
        .alias(VarActif.mtPfi),
    ]).with_columns(

        pl.when(rsVente)
        .then(pl.col(VarActif.mtVmAv) - pl.col(VarActif.mtVm))
        .otherwise(pl.col(VarActif.mtCf))
        .alias(VarActif.mtCf)

    ).with_columns([
        
        pl.when(rsAchat)
        .then(pl.col(VarActif.mtVmAv) * pl.col(VarStratInv.facteurAchatVente))
        .otherwise(pl.col(VarActif.mtVm))
        .alias(VarActif.mtVm),

        pl.when(rsAchat)
        .then(pl.col(VarActif.mtVcAv) + pl.col(VarActif.mtVm) - pl.col(VarActif.mtVmAv))
        .otherwise(pl.col(VarActif.mtVc))
        .alias(VarActif.mtVc),
    
    ]).with_columns([
        pl.when(rsAchat)
        .then(pl.col(VarActif.mtVmAv) - pl.col(VarActif.mtVm))
        .otherwise(pl.col(VarActif.mtCf))
        .alias(VarActif.mtCf),
        pl.lit(0.0).alias(VarActif.mtPfi)

    ]).with_columns([
        pl.when(rsCash)
        .then(pl.col(VarActif.mtCf) * -1.0)
        .otherwise(pl.col(VarActif.mtCf))
        .alias(VarActif.mtCf),
        pl.when(rsCash)
        .then(pl.lit(0.0))
        .otherwise(pl.col(VarActif.mtPfi))
        .alias(VarActif.mtPfi),
        pl.lit(0.0).alias(VarAlm.mtFuiteVc),
        pl.lit(0.0).alias(VarAlm.mtFuiteEco),
        calcPmvl().alias(VarActif.mtPmvl)
    ])

    return mpActifProj
