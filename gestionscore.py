
from __future__ import annotations
from fonction import *
from typing import BinaryIO
import pickle

class score:
    pseudo : str
    nbpoints : int

def ajoutscore(jeux : str,scorejeux : score):
    """
    ouvre le fichier score et lui implémente le scorde d'un jeu .
    entrée : 
        jeux(str) : une chaine de caractère qui représente le nom du jeu
        scorejeux(score) :le nom du joueur en chaine de caractère et le score en entier"""
    f1 : BinaryIO
    f2 : BinaryIO
    f3 : BinaryIO
    if jeux=='devinette':
        f1=open("scoredevinette","ab+")#ab+ Ouvre un fichier à la fois pour l'ajout et la lecture en format binaire. Le pointeur de fichier se trouve à la fin du fichier si le fichier existe. Le fichier s'ouvre en mode append. Si le fichier n'existe pas, il crée un nouveau fichier pour la lecture et l'écriture.
        pickle.dump(scorejeux,f1)
        f1.close()
    if jeux=='allumette':
        f2=open("scoreallumette","ab+")
        pickle.dump(scorejeux,f2)
        f2.close()
    if jeux=='morpion':
        f3=open("scoremorpion","ab+")
        pickle.dump(scorejeux,f3)
        f3.close()

    
def affichagescore():
    """
    Affiche le menu de score ouvre et affiche le fichier binaire de score du jeu choisit et implémente les nouveau score en les triant ."""
    f1 : BinaryIO #fichier binaire
    f2 : BinaryIO #fichier binaire
    f3 : BinaryIO #fichier binaire
    ls : list[int] #liste des pseudo
    lp : list[str] #liste des points
    s : score
    n:int #nombre de pseudo
    i : int
    j : int
    k : int
    choix : str
    print(
"""
+==========================+
| ____                     |
|/ ___|  ___ ___  _ __ ___ |
|\___ \ / __/ _ \| '__/ _ \|
| ___) | (_| (_) | | |  __/|
||____/ \___\___/|_|  \___||
+==========================+

"""
)
    print("-------------------------------------------------")
    print("| De quel jeux voulez vous voir les scores :    |")
    print("|                1 - devinette                  |")
    print("|                2 - allumettes                 |")
    print("|                3 - morpion                    |")
    print("|                4 - quitter                    |") 
    print("-------------------------------------------------")
    choix=input("Quel est votre choix (1,2,3 ou 4) : ") #choix du menu
    while not est1nombre(choix):
        print("Erreur, choisissez une des options ci-dessus")
        choix=input("Quel est votre choix (1,2,3 ou 4) : ")
    while int(choix)!=1 and int(choix)!=2  and int(choix)!=3  and int(choix)!=4 : #test si le choix et valide
        print("Erreur, choisissez une des options ci-dessus")
        choix=input("Quel est votre choix (1,2,3 ou 4) : ")
        while not est1nombre(choix): #test si le choix et bien un entier
            print("Erreur, choisissez une des options ci-dessus")
            choix=input("Quel est votre choix (1,2,3 ou 4) : ")
    s=score()
    ls=[]
    lp=[]
    i=0
    if int(choix)==1: #ouvre le fichier de score des divenettes et l'affiche
        f1=open("scoredevinette","rb")
        fin=False
        while not fin :
            try :

                s=pickle.load(f1)                
                ls.append(s.nbpoints)
                lp.append(s.pseudo)
                i=i+1
            except EOFError :
                fin = True
        f1.close()
    if int(choix)==2: #ouvre le fichier de score des allumettes et l'affiche
        f2=open("scoreallumette","rb")
        fin=False
        while not fin :
            try :
                s=pickle.load(f2)
                ls.append(s.nbpoints)
                lp.append(s.pseudo)                
                i=i+1
            except EOFError :
                fin = True
        f2.close()
    if int(choix)==3: #ouvre le fichier de score des morpions et l'affiche
        f3=open("scoremorpion","rb")
        fin=False
        while not fin :
            try :
                s=pickle.load(f3)
                ls.append(s.nbpoints)
                lp.append(s.pseudo)
                i=i+1
            except EOFError :
                fin = True
        f3.close()
    n = len(ls)
    for k in range(n): #trie les score du plus grand au plus petit
        for j in range(0, n-k-1):
            if ls[j] < ls[j+1] :
                ls[j], ls[j+1] = ls[j+1], ls[j]
                lp[j], lp[j+1] = lp[j+1], lp[j]
    for j in range(0,i):
        print(f'              {j+1}.{(4-len(str(j+1)))*" "}{lp[j]}{(20-len(lp[j]))*" "}: {ls[j]} points')
























