from enum import StrEnum
import re

class StrEnumCaps(StrEnum):
    """
    Classe héritant de StrEnum permettant dans le code de nommer les variables mtVm et d'avoir comme valeur MT_VM
    """
    def _generate_next_value_(name, start, count, last_values):
        nameUpperParts = re.findall('[A-Z][^A-Z]*', name)
        namePrefix =  name.replace(''.join([nameSplitEl for nameSplitEl in nameUpperParts]), '')
        nameElementList = []
        nameElementList.append(namePrefix)
        nameElementList.extend(nameUpperParts)
        return "_".join([nameEl.upper() for nameEl in nameElementList])
    
class StrEnumLower(StrEnum):
    """
    Classe héritant de StrEnum permettant dans le code de nommer les variables mtVm et d'avoir comme valeur MT_VM
    """
    def _generate_next_value_(name, start, count, last_values):
        nameUpperParts = re.findall('[A-Z][^A-Z]*', name)
        namePrefix =  name.replace(''.join([nameSplitEl for nameSplitEl in nameUpperParts]), '')
        nameElementList = []
        nameElementList.append(namePrefix)
        nameElementList.extend(nameUpperParts)
        return "_".join([nameEl.lower() for nameEl in nameElementList])

class StrEnumIso(StrEnum):
    """
    Classe héritant de StrEnum permettant dans le code de nommer les variables mtVm et d'avoir comme valeur MT_VM
    """
    def _generate_next_value_(name, start, count, last_values):
        return name