
from __future__ import annotations
def afflogo():
    """Affiche le logo ."""
    print(
"""
4+========================================================================+
| __  __ _       _     _                    __         _                 |
||  \/  (_)_ __ (_)   (_) ___ _   ___  __   \_\_    __| | ___ _   ___  __|
|| |\/| | | '_ \| |   | |/ _ \ | | \ \/ /  / _` |  / _` |/ _ \ | | \ \/ /|
|| |  | | | | | | |   | |  __/ |_| |>  <  | (_| | | (_| |  __/ |_| |>  < |
||_|  |_|_|_| |_|_|  _/ |\___|\__,_/_/\_\  \__,_|  \__,_|\___|\__,_/_/\_\|
|                   |__/                                                 |
+========================================================================+
"""
    )
def affmenu()->int:
    """
    Affiche le menu de tout les jeux et prend le choix du joueur en saisie .
    sortie : Un entier qui représente le choix du joueur
    """
    saisie : str
    print("Voici les options disponibles : ")
    print("-------------------------------")
    print("| 1 - Jouer aux devinettes     |")
    print("| 2 - Jouer aux allumettes     |")
    print("| 3 - Jouer au morpion         |")
    print("| 4 - Voir les scores          |")
    print("| 5 - Quitter                  |") 
    print("-------------------------------")   
    saisie=input("Que voulez-vous faire :")    
    while not est1nombre(saisie):
        print("Erreur, le choix n'est pas valide")
        saisie=input("Que voulais vous faire")
    while int(saisie)!=1 and int(saisie)!=2 and int(saisie)!=3 and int(saisie)!=4 and int(saisie)!=5:
        print("Erreur, le choix n'est pas valide")
        saisie=input("Que voulais vous faire")    
        while not est1nombre(saisie):
            print("Erreur, le choix n'est pas valide")
            saisie=input("Que voulais vous faire") 
    return int(saisie)

from gestionscore import *
from fonction import *
from devinette import *
from allumette import *
from morpion import *

if __name__ == "__main__":
    choix : int
    afflogo()
    choix=affmenu()
    while choix!=5:
        if choix==1:
            devinnb()
        if choix==2:
            jeuallumette()
        if choix==3:
            jeumorpion()
        if choix==4:
            affichagescore()
        choix=affmenu()
    print("Au revoir")