
from __future__ import annotations
def est1nombre(chaine : str) -> bool:
    """
        Vérifie si la chaîne de caractères est un entier.
 
        Entrée:
            chaine (str): La chaîne de caractères à vérifier.
 
        Retourne:
            bool: True si la chaîne est un entier, False sinon.
    """
    nombre : str
    est1nombre : bool
    i : int
 
    if chaine == "":
        return False
    nombre = "0123456789"
    est1nombre = True
    i  = 0
    while i < len(chaine) and est1nombre:
        if chaine[i] not in nombre: 
            est1nombre = False
        i = i+1
    return est1nombre


def choixpseudo(numjoueur : int)->str:
    """
    Choix du pseudo du joueur suivant son numéro .
    entrée : 
        numjoueur(entier): qui représente le numèro du joueur
    sortie : Une chaine de caractère qui eprésente le pseudo du joueur choisit 
    """
    pseudo : str
    print("Joueur ",numjoueur," : saisissez votre pseudo (max 15 caractères et différent de 'bot 1' et 'bot 2')")
    pseudo=input("Quel est votre choix : ")
    while pseudo=='' or len(pseudo)>15 or pseudo=='bot 1' or pseudo=='bot 2':
        print("Erreur")
        print("Joueur ",numjoueur," : saisissez votre pseudo (max 15 caractères et différent de 'bot')")
        pseudo=input("Quel est votre choix : ")
    return pseudo

def testpseudo(pseudo1 : str, pseudo2 : str)->bool:
    """
    Teste si deux pseudo son identique
    entrée : le pseudo des deux joueur
    sortie : un booléen qui vaut vraie si les deux pseudos sont différents
    """
    test : bool
    test = True
    if pseudo1==pseudo2:
        test=False
        print("Erreur, choisissez 2 pseudos différents s'il vous plait.")
    return test