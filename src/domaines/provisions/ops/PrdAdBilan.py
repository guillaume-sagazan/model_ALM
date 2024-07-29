from typing import Tuple
import polars as pl
from polars import DataFrame

from metadata.dd.DdActif import VarActif
from metadata.dd.DdAlm import VarAlm, CdMethodeInitEquilibreBilan
from metadata.dd.DdPassifEp import VarPassif
from metadata.dfmd.DfMdActif import dfMdActif
from metadata.dfmd.DfMdAlmCr import dfMdAlmCr
from metadata.dfmd.DfMdPassifEp import dfMdPassifEp


def prdAdBilanInit(projActifCash:DataFrame, projActifOblig:DataFrame, projActifIndices:DataFrame,
                    projPassifEpMp:DataFrame,
                    projProvOther:DataFrame, projProvPpe:DataFrame,
                    methodeInitEquilibreBilan:CdMethodeInitEquilibreBilan
                    ) -> Tuple[DataFrame, DataFrame]:

    """Méthode en charge d'équilibrer le bilan à l'initialisation du modèle
    :param projActifCash: Cash
    :type projActifCash: DataFrame[ProjActif]
    :param projActifOblig: Titres obligataires
    :type projActifOblig: DataFrame[ProjActif]
    :param projActifIndices: Actifs indiciels
    :type projActifIndices: DataFrame[ProjActif]
    :param projPassifEpMp: Contrats Supports
    :type projPassifEpMp: DataFrame[ProjPassifEpMp]
    :param projProvOther: Provisions comptables
    :type projProvOther: DataFrame[ProjProvOther]
    :param projProvPpe: Générations de PPB
    :type projProvPpe: DataFrame[ProjProvOther]
    :return: Cash et provisions comptables
    :rtype: DataFrame[ProjActif], DataFrame[ProjProvOther]
    """
    
    prdAdBilan = prdAdBilanCalc(projActifCash=projActifCash, projActifOblig=projActifOblig, projActifIndices=projActifIndices,
                                     projPassifEpMp=projPassifEpMp,
                                     projProvOther=projProvOther, projProvPpe=projProvPpe) \
                    .rename({VarAlm.mtFuiteVc:VarAlm.mtFuiteVcTmp})

    mdPrdAdBilan = dfMdAlmCr.mdPrdAdBilan
    mdProjActif = dfMdActif.mdProjActif
    mdProjProvOther = dfMdAlmCr.mdProjProvOther

    if methodeInitEquilibreBilan == CdMethodeInitEquilibreBilan.CASH:
        projActifCash = projActifCash.join(
                prdAdBilan.select([*mdPrdAdBilan.pks, VarAlm.mtFuiteVcTmp]),
                how='left',
                on=mdPrdAdBilan.pks
            ).with_columns([
                (pl.col(VarActif.mtVm) + pl.col(VarAlm.mtFuiteVcTmp)).alias(VarActif.mtVm),
                (pl.col(VarActif.mtVc) + pl.col(VarAlm.mtFuiteVcTmp)).alias(VarActif.mtVc),
            ])                         

    elif methodeInitEquilibreBilan == CdMethodeInitEquilibreBilan.FONDS_PROPRES:
        projProvOther = projProvOther.join(
            prdAdBilan.select([*mdPrdAdBilan.pks, VarAlm.mtFuiteVcTmp]),
                how='left',
                on=mdPrdAdBilan.pks
            ).with_columns(
                (pl.col(VarAlm.mtCapitauxPropres) - pl.col(VarAlm.mtFuiteVcTmp)).alias(VarAlm.mtCapitauxPropres)
            )

    return projActifCash.select(mdProjActif.allColumns), projProvOther.select(mdProjProvOther.allColumns)

def prdAdBilanCalc(projActifOblig:DataFrame, projActifIndices:DataFrame, projActifCash:DataFrame,
                    projPassifEpMp:DataFrame,
                    projProvOther:DataFrame, projProvPpe:DataFrame) -> DataFrame:

    """Méthode en charge de calculer le dataframe PrdAdBilan
    :param projActifOblig:
    :type projActifOblig: DataFrame
    :param projActifIndices:
    :type projActifIndices: DataFrame
    :param projActifCash:
    :type projActifCash: DataFrame
    :param projPassifEpMp:
    :type projPassifEpMp: DataFrame
    :param projProvOther:
    :type projProvOther: DataFrame
    :param projProvPpe: Générations de PPB
    :type projProvPpe: DataFrame

    :return: DataFrame au format PrdAdBilan
    :rtype: DataFrame

    """
    mdPrdAdBilan = dfMdAlmCr.mdPrdAdBilan
    mdProjActif = dfMdActif.mdProjActif
    mdProjPassifEpMp = dfMdPassifEp.mdProjPassifEpMp

    prdAdBilan = projProvOther

    if not projActifOblig is None and not projActifOblig is None and not projActifOblig is None:
        projActifCanton = pl.concat([
                projActifOblig.select([*mdProjActif.pks, VarActif.mtVc, VarActif.mtPdd]), 
                projActifIndices.select([*mdProjActif.pks, VarActif.mtVc, VarActif.mtPdd]), 
                projActifCash.select([*mdProjActif.pks, VarActif.mtVc, VarActif.mtPdd])
            ]).group_by(mdPrdAdBilan.pks).sum()
        prdAdBilan = prdAdBilan.join(projActifCanton, how='left', on=mdPrdAdBilan.pks)

    if not projPassifEpMp is None:
        projPassifEpMpCanton = projPassifEpMp.select([*mdProjPassifEpMp.pks, VarPassif.mtPm]) \
                .group_by(mdPrdAdBilan.pks).sum()
        prdAdBilan = prdAdBilan.join(projPassifEpMpCanton,
                                     how='left',
                                     on=mdPrdAdBilan.pks)

    if not projProvPpe is None:
        projProvPpeCanton = projProvPpe.group_by(mdPrdAdBilan.pks).sum()
        prdAdBilan = prdAdBilan.join(projProvPpeCanton,
                                     how='left',
                                     on=mdPrdAdBilan.pks)

    prdAdBilan = prdAdBilan.with_columns(
        (
            pl.col(VarPassif.mtPm)
            + pl.col(VarAlm.mtPpe)
            + pl.col(VarActif.mtPre)
            + pl.col(VarActif.mtPdd)
            + pl.col(VarAlm.mtReserveCapi)
            + pl.col(VarAlm.mtCapitauxPropres)
            - pl.col(VarActif.mtVc)
        ).alias(VarAlm.mtFuiteVc)
    )

    return prdAdBilan