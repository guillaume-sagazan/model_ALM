Exemples de code
================

Formules unitaires réutilisables
--------------------------------

Ci-dessous deux exemples de définition d'expressions polars :

.. code-block:: python
    :caption: Expression polars permettant de filtrer sur les chocs S2 Equity

    def rsCdChocS2Equity() -> pl.Expr:
        return pl.col(VarS2.cdChocS2) == CdChocS2.equity


.. code-block:: python
    :caption: Expression calculant de la valeur de marché action choquée S2
    
    def calcMtVmEquityChocS2(colMtVm : str = VarActif.mtVm, alias : str = VarActif.mtVm) -> pl.Expr:
        expr = pl.col(colMtVm) * (
            1.
            + pl.col(VarS2.txChocEquityT1) * pl.col(VarActif.txActionT1)
            + pl.col(VarS2.txChocEquityT2) * pl.col(VarActif.txActionT2)
            + pl.col(VarS2.txChocEquityStrat) * pl.col(VarActif.txActionStrat)
            )
        
        if alias is not None:
            expr = expr.alias(alias)
        
        return expr 

.. code-block:: python
    :caption: Formule de calcul de la valeur de marché des actifs indiciels à l'initialisation du modèle 

    def calcMtVmIndicesInitS2(colMtVm : str = VarActif.mtVm, alias : str = VarActif.mtVm) -> pl.Expr:
        expr = pl.when(rsCdChocS2Equity()) \
                .then(calcMtVmChocEquity(colMtVm=colMtVm, alias=None)) \
                .when(rsCdChocS2Property()) \
                .then(calcMtVmChocProperty(colMtVm=colMtVm, alias=None)) \
                .otherwise(pl.col(VarActif.mtVm))
        
        if alias is not None:
            expr = expr.alias(alias)

        return expr

Pipelines de données réutilisables
----------------------------------

Ci-dessous un exemple d'une telle transformation :

.. code-block:: python

    def projActifIndicesPerf(period: int,
                      projActifIndices: DataFrame,
                      gseOutputIndicesPerfT: DataFrame,
                      gseCtRefCashPerfT: DataFrame) -> Tuple[DataFrame, DataFrame]:

        """Méthode appliquant l'évènement "performance" sur une DataFrame projActifIndices

        L'application de la performance sur le cash implique :
        * de faire une copie du dataframe d'entrée
        * renseigner dans cette copie le scenario, l'itération et l'évènement (Perf)
        * d'appliquer le taux de performance du cash sur la base du DataFrame gseOutputIndicesPerfT
        * de calculer la fuite économique comme la différence entre l'augmentation de VM sur la base du taux de performance du cash appliqué et du taux de performance du cash attendu dans le cadre du scenario CRN

        :param period: période
        :type period: int
        :param projActifIndices: DataFrame projActifIndices en entrée
        :type projActifIndices: DataFrame
        :param gseOutputIndicesPerfT: Taux de performance du cash à appliquer pour le scenario et l'itération
        :param gseCtRefCashPerfT: Taux de performance attendu dans le cadre du scenario CRN
        :return: DataFrame projActifIndices mis à jour

        """

        mdProjActif = dfMdActif.mdProjActif

        newProjActifIndices = projActifCopy(projActifIndices, period=period, evenement=ModeleAlmEvenement.Perf)

        newProjActifIndices = newProjActifIndices.join(
            gseOutputIndicesPerfT,
            how='left',
            on=[VarS2.cdChocS2Gse, VarActif.cdClasseActif, VarProj.period],
        ).with_columns(
            pl.lit(IntraPeriod.BEG).alias(VarProj.intraperiod)
        ).join(gseCtRefCashPerfT,
            how='left',
            on=[VarS2.cdChocS2Gse, VarProj.period, VarProj.intraperiod],
            suffix='_ct_ref'
        ).with_columns([
            (pl.col(VarGse.facteurPerfNet) * pl.col(VarActif.mtVmAv)).alias(VarActif.mtVm),
            (pl.col(VarActif.mtVmAv) * pl.col(VarGse.txDividendes)).alias(VarActif.mtPfi),
            (pl.col(VarActif.mtVmAv) * pl.col(VarGse.txDividendes)).alias(VarActif.mtCf),
            pl.lit(0.0).alias(VarActif.mtPdd)
        ]).with_columns([
            calcPmvl().alias(VarActif.mtPmvl),
            calcFuiteEco().alias(VarAlm.mtFuiteEco),
            calcFuiteVcActifPerf().alias(VarAlm.mtFuiteVc)
        ])
        
        projActifCashPerfInputCf = projActif2projActifCashPerfInputCf(newProjActifIndices)

        return newProjActifIndices.select(mdProjActif.allColumns), projActifCashPerfInputCf


Exemple d'implémentation d'un évènement
---------------------------------------

.. code-block:: python

    def fnProjPerfActif(period:int,
                    mpActifOblig:DataFrame, projActifObligCf:DataFrame,
                    projActifOblig:DataFrame, projActifIndices:DataFrame, projActifCash:DataFrame,
                    gseOutputObligPzcT:DataFrame, gseOutputIndicesPerfT:DataFrame, gseOutputCashPerfT:DataFrame,
                    gseCtRefCashPerfT:DataFrame,
                    projActifCashPerfInputCfTList:list,
                    projResultRctProjActif: ProjResultRctProjActif,
                    projResultPrdAd:ProjResultPrdAd) -> Tuple[DataFrame,DataFrame,DataFrame,DataFrame,DataFrame,DataFrame,DataFrame,DataFrame]:

    logging.info(f'Perf ({period}) : Actif : Obligations / Actions / Immobilier')
    projActifOblig, projActifObligCf, mpActifOblig, projActifObligCashPerfInputCf = \
        projActifObligPerf(period, projActifOblig, projActifObligCf, mpActifOblig,
                        gseOutputObligPzcT, gseCtRefCashPerfT)

    projActifCashPerfInputCfTList.append(projActifObligCashPerfInputCf)

    projActifIndices, projActifIndicesCashPerfInputCf = \
        projActifIndicesPerf(period, projActifIndices, gseOutputIndicesPerfT,
                          gseCtRefCashPerfT)

    projActifCashPerfInputCfTList.append(projActifIndicesCashPerfInputCf)

    projActifCashPerfInputCf = pl.concat(projActifCashPerfInputCfTList)
    projActifCashPerfInputCfTList = []

    # projActifCashPerfInputCf = pl.concat([projActifObligCashPerfInputCf, projActifIndicesCashPerfInputCf])
    logging.info(f'Perf ({period}) : Actif : Impact du cash')
    projActifCash = projActifCashPerf(period, projActifCash, projActifCashPerfInputCf, gseOutputCashPerfT,
                                gseCtRefCashPerfT)

    logging.info(f'Perf ({period}) : Actif : Construction du PrdAdActif')
    projActifPerfT = pl.concat([projActifOblig, projActifIndices, projActifCash])
    prdAdActifPerfT = prdAdActifBuild(projActifPerfT)

    logging.info(f'Perf ({period}) : Actif : Append dans les listes de résultats')
    projResultPrdAd.appendOutputPrdAdPrdAdActif(prdAdActifPerfT)
    projResultRctProjActif.appendOutputRctProjProjActif(projActifPerfT)
    projResultRctProjActif.appendOutputRctProjActifObligCf(projActifObligCf=projActifObligCf,
                                                 period=period, evenement=ModeleAlmEvenement.Perf)
    projResultRctProjActif.appendOutputRctProjprojActifCashPerfInputCf(projActifCashPerfInputCf)

    return projActifOblig, projActifObligCf, mpActifOblig, projActifObligCashPerfInputCf, \
        projActifIndices, projActifIndicesCashPerfInputCf, \
        projActifCash, projActifCashPerfInputCf, \
        projActifPerfT, prdAdActifPerfT

Orchestrateur
-------------

L'orchestrateur est un composant central de l'implémentation. Il permet de définir l'ordre d'exécution des différents évènements.

Voir code source.
