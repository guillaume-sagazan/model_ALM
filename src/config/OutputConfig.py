from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

@dataclass
class ResultsWriterScConfig:
    pass

@dataclass_json
@dataclass
class OutputConfig:
    
    """Classe stockant la ProjConfig associée à la gestion des erreurs d'une projection
    
    :param genererOutputDebug: Booléen activant l'écriture des outputs de debug. Valeur par défaut = True
    :type genererOutputDebug: bool
    :param genererOutputDebugScListStr: Liste des scenarios pour lesquels les outputs de debug seront écrits au format chaine de caractères. Valeur par défaut = '1'
    :type genererOutputDebugScListStr: str
    :param genererOutputDebugScList: Liste des scenarios pour lesquels les outputs de debug seront écrits au format liste d'entier. Initialisé dans la méthode __post_init__ à partir de writeOutputDebugScListStr
    :type writeOutputDebugScList: list[int]
    :param genererOutputRctLoad: Booléen activant l'écriture des outputs de recette associés au chargement des données et hypothèses du Passif. Valeur par défaut = True
    :type genererOutputRctLoad: bool
    :param genererOutputRctInitGse: Booléen activant l'écriture des outputs de recette associés au GSE post initialisation. Valeur par défaut = True
    :type genererOutputRctInitGse: bool
    :param genererOutputRctInitActif: Booléen activant l'écriture des outputs de recette associés à l'Actif post initialisation. Valeur par défaut = True
    :type genererOutputRctInitActif: bool
    :param genererOutputRctInitPassif: Booléen activant l'écriture des outputs de recette associés au Passif post initialisation. Valeur par défaut = True
    :type genererOutputRctInitPassif: bool
    :param genererOutputRctProjActif: Booléen activant l'écriture des outputs de recette associés à l'Actif durant la projection. Valeur par défaut = True
    :type genererOutputRctProjActif: bool
    :param genererOutputRctProjPassif: Booléen activant l'écriture des outputs de recette associés au Passif durant la projection. Valeur par défaut = True
    :type genererOutputRctProjPassif: bool
    :param genererOutputRctProjStratInv: Booléen activant l'écriture des outputs de recette associés à la stratégie d'investissement durant la projection. Valeur par défaut = True
    :type genererOutputRctProjStratInv: bool
    :param genererOutputRctProjProv: Booléen activant l'écriture des outputs de recette associés aux Provisions durant la projection. Valeur par défaut = True
    :type genererOutputRctProjProv: bool
    :param genererOutputRctProjAlmCr: Booléen activant l'écriture des outputs de recette associés à la stratégie ALM durant la projection. Valeur par défaut = True
    :type genererOutputRctProjAlmCr: bool
    :param genererOutputRctScListStr: Liste des scenarios pour lesquels les outputs de recette seront écrits au format chaine de caractères. Valeur par défaut = '1'
    :type genererOutputRctScListStr: str
    :param genererOutputRctScList: Liste des scenarios pour lesquels les outputs de recette seront écrits au format liste d'entiers. Initialisé dans la méthode __post_init__ à partir de writeOutputRctScListStr
    :type writeOutputRctScList: list[int]
    :param genererOutputPrdAd: Booléen activant l'écriture des outputs de production nécessaire à l'alimentation du template Analyse Déterministe. Valeur par défaut = True
    :type genererOutputPrdAd: bool
    :param genererOutputPrdAdScListStr: Liste des scenarios pour lesquels les outputs de production Analyse Déterministe seront écrits au format chaine de caractères. Valeur par défaut = '1'
    :type genererOutputPrdAdScListStr: str
    :param genererOutputPrdAdScList: Liste des scenarios pour lesquels les outputs de production Analyse Déterministe seront écrits au format liste d'entiers. Initialisé dans la méthode __post_init__ à partir de writeOutputPrdAdScListStr
    :type writeOutputPrdAdScList: list[int]
    :param genererOutputPrdQrt: Booléen activant l'écriture des outputs permettant d'alimenter les Qrt. Valeur par défaut = True
    :type genererOutputPrdQrt: bool

    """

    genererOutputDebug : bool = field(default = True)
    genererOutputRctLoad : bool = field(default = True)
    genererOutputRctInitGse : bool = field(default = True)
    genererOutputRctInitActif: bool = field(default = True)
    genererOutputRctInitPassif: bool = field(default=True)
    genererOutputRctProjActif : bool = field(default = True)
    genererOutputRctProjPassif: bool = field(default=True)
    genererOutputRctProjStratInv : bool = field(default = True)
    genererOutputRctProjProv: bool = field(default=True)
    genererOutputRctProjAlmCr : bool = field(default = True)
    genererOutputPrdAd : bool = field(default = True)
    genererOutputPrdQrt: bool = field(default = True)

