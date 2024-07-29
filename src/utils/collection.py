import re

def checkListContained(A:list, B:list)->bool:
    """
    Cette fonction permet de vérifier si la liste A est contenue dans la liste B

    :param A: Première liste
    :param B: Seconde liste

    :returns: Booléen Vrai / Faux
    """
    # # convert list A to numpy array
    # A_arr = np.array(A)
    # # convert list B to numpy array
    # B_arr = np.array(B)

    # for i in range(len(B_arr)):
    #     if np.array_equal(A_arr, B_arr[i:i + len(A_arr)]):
    #         return True
    # return False
    pass

def convertStringToIntList(s : str) -> list :
    """
    Cette fonction permet de convertir une string au format "1-10,40,50-100" en une liste d'entiers

    :param s: string à convertir en liste d'entier
    :returns: Liste d'entier
    """
    result : list = []
    if s != '':
        list1 = s.split(',')
        for list1item in list1:
            list1item_split = list1item.split('-')
            if len(list1item_split) == 1:
                result.append(int(list1item))
            elif len(list1item_split) == 2:
                result.extend([*range(int(list1item_split[0]), int(list1item_split[1])+1)])
            else:
                raise Exception("convertStringToIntList(" + s + ") not working !")
        result.sort()
    return result

def listIntersection(lst1:list, lst2:list)->list:
    """
    Cette fonction retourne l'intersection de 2 listes

    :param lst1: Première liste d'éléments
    :param lst2: Seconde liste d'éléments

    :returns: Intersection des listes lst1 et lst2
    """
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def listUnion(lstOfLst : list):
    """
    Cette fonction retourne l'union des listes en entrée

    :param lstOfLst: liste de liste à prendre en compte

    :returns: Liste correspondant à l'union des listes en entrée
    """
    if len(lstOfLst) == 0:
        return []

    result = []

    for lst in lstOfLst:
        if result == []:
            result = lst.copy()
        else:
            for el in lst:
                if el not in result:
                    result.append(el)

    return result

def isStrInListFullMatch(s:str, strList:list[str]) -> bool:
    """
    Cette fonction vérifie si la chaîne de caractère s est présente dans la liste strList

    :param s: chaine de caractère
    :param strList: liste de chaine de caractères dans laquelle rechercher

    :returns: Booléen vrai / faux
    """
    result = False
    for el in strList:
        result = result or re.fullmatch(el, s)
    return result

def isStrInListMatch(s:str, strList:list[str]) -> bool:

    """Méthode permettant de vérifier si une chaîne de caractère s est présente dans une liste de string

    :param s: chaine de caractères recherchée
    :param strList: liste de chaîne de caractères dans laquelle rechercher

    :returns: Booléen vrai / faux

    """
    result = False
    for el in strList:
        result = result or re.match(el, s)
    return result