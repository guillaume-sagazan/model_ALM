from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from enum import IntEnum

class OnErrorStrategy(IntEnum):
    """Enumération permettant de définir la stratégie à suivre dans le cas où des erreurs sont détectées
    :param CONTINUER: Dans ce cas, le programme a vocation à continuer malgré les erreurs constatées
    :param LANCER_EXCEPTION: Dans ce cas, le programme lancera une exception au moment de la détection de l'erreur
    """
    CONTINUER = 1
    LANCER_EXCEPTION = 2

@dataclass_json
@dataclass
class ErrConfig :
    
    """Classe stockant la ProjConfig associée à la gestion des erreurs d'une projection

    :param errorZero: Définition du zéro absolu dans le cadre du traitement. Valeur par défaut = 0.000000000001
    :type errorZero: float
    :param errorZeroRelatif: Définition du zéro relatif dans le cadre du traitement. Valeur par défaut = 0.0000000001
    :type errorZeroRelatif: float
    :param initPassifErrorStrategy: Stratégie adoptée en cas d'erreur constatée à l'initialisation du Passif. Valeur par défaut = OnErrorStrategy.CONTINUER
    :type initPassifErrorStrategy: OnErrorStrategy
    :param initActifObligTraIterMax: Maximum d'itérations maximums associée à l'initialisation du TRA. Valeur par défaut = 10000
    :type initActifObligTraIterMax: int
    :param initActifErrorStrategy: Stratégie adoptée en cas d'erreur constatée à l'initialisation de l'Actif. Valeur par défaut =  OnErrorStrategy.CONTINUER
    :type initActifErrorStrategy: OnErrorStrategy
    :param equilibreBilanErrorStrategy: Stratégie adoptée en cas d'erreur bilan constatée. Valeur par défaut = OnErrorStrategy.CONTINUER
    :type equilibreBilanErrorStrategy: OnErrorStrategy
    :param equilibreBilanErrorMax: Maximum tolérer pour l'écart d'erreur bilan. Valeur par défaut = 20.0
    :type equilibreBilanErrorMax: float
    
    """

    errorZero: float = field(default = 0.000000000001)
    errorZeroRelatif: float = field(default = 0.0000000001)

    initPassifErrorStrategy: OnErrorStrategy = field(default=OnErrorStrategy.CONTINUER)

    initActifObligTraIterMax: int = field(default=10000)
    initActifErrorStrategy: OnErrorStrategy = field(default = OnErrorStrategy.CONTINUER)

    equilibreBilanErrorStrategy: OnErrorStrategy = field(default = OnErrorStrategy.CONTINUER)
    equilibreBilanErrorMax: float = field(default=20.0)




