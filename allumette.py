#programmme allumette 
from __future__ import annotations
from random import *
from time import *
def enlevéallumette(res : int ,choix : int)->int:
    """
    Enlève le nombre d'allumette choisit au nombre d'allumettes restante .
    entrée : 
        res(entier) : le nombre d'allumettes
        choix(entier) : le nombre d'alumettes à enlever 
    sortie :Le nombre d'allumettes restantes .
    """
    res : int 
    res = res - choix
    return res
from gestionscore import *
from fonction import *
def jeuallumette():
    """
    Procédure principale du jeux des allumettes
    """
    nballu : int #nombre totale d'allumettes
    allu : str #nombre totale d'allumettes en représentation graphique
    choix : int #choix du joueur
    saisie : str #choix du joueur en chaine de caractère
    numjoueur : int
    allj1 : int #choix du joueur 1
    allj2 : int #choix du joueur 2
    choixIA : int #choix de l'ordinateur
    scoreallumettej1 : score
    scoreallumettej2 : score    
    print(
"""
+==============================================+
|    _    _ _                      _   _       |
|   / \  | | |_   _ _ __ ___   ___| |_| |_ ___ |
|  / _ \ | | | | | | '_ ` _ \ / _ \ __| __/ _ \|
| / ___ \| | | |_| | | | | | |  __/ |_| ||  __/|
|/_/   \_\_|_|\__,_|_| |_| |_|\___|\__|\__\___||
+==============================================+
"""
    )
    scoreallumettej1=score()
    scoreallumettej2=score()
    allj1=0
    allj2=0
    nballu = 20
    allu = '| '
    choixIA=0
    numjoueur=1
    jeux='allumette'
    print("------------------------------------")
    print("|                                  |")
    print("| 1 - Jouer à 2 joueurs            |")
    print("| 2 - Jouer contre l'ordinateur    |")
    print("| 3 - Ordinateur contre ordinateur |")
    print("| 4 - Quitter                      |")
    print("|                                  |")
    print("------------------------------------")
    saisie=input("Faites votre choix :")
    while saisie!='1' and saisie!='2' and saisie!='3':
        saisie=input("Erreur ce n'est pas un choix valide. Faites votre choix :")
    if saisie == '1' : 
        #saisie du nom des joueurs et test de leurs validité
        pseudo1=choixpseudo(numjoueur)
        numjoueur=2
        pseudo2=choixpseudo(numjoueur)
        while not testpseudo(pseudo1,pseudo2):
            numjoueur=1
            pseudo1=choixpseudo(numjoueur)
            numjoueur=2
            pseudo2=choixpseudo(numjoueur)
        print("Il reste ",nballu," allumettes")
        while nballu>0 :# test si il reste des allumettes
            
            print(pseudo1," - Combien voulez vous enlever d'allumettes (1,2 ou 3) : ") #saisie du joueur 1
            saisie=input()

            while est1nombre(saisie)==False or (int(saisie)!=1 and int(saisie)!=2 and int(saisie)!=3) or int(saisie)>nballu: #test si la saisie est valide pour le joueur 1
                print("Erreur ce n'est pas un nombre possible d'allumettes restantes(1,2 ou 3) ")
                print(pseudo1," - Combien voulez vous enlever d'allumettes (1,2 ou 3) : ")
                saisie=input()
            choix=int(saisie)
            allj1=allj1 + choix
            nballu=enlevéallumette(nballu ,choix)
            if nballu>=0:
                numjoueur = 2    
            print(nballu*allu)
            print("Il reste ",nballu," allumettes")
            if nballu>0 :# test si il reste des allumettes
                
                print(pseudo2," - Combien voulez vous enlever d'allumettes (1,2 ou 3) : ") #saisie du joueur 2
                saisie=input()

                while est1nombre(saisie)==False or (int(saisie)!=1 and int(saisie)!=2 and int(saisie)!=3) or int(saisie)>nballu: #test si la saisie est valide pour le joueur 2
                    print("Erreur ce n'est pas un nombre possible d'allumettes restantes(1,2 ou 3) ")
                    print(pseudo2," - Combien voulez vous enlever d'allumettes (1,2 ou 3) : ")
                    saisie=input()
                choix=int(saisie)
                allj2=allj2 + choix
                nballu=enlevéallumette(nballu ,choix)
                if nballu>=0: 
                    numjoueur = 1
                print(nballu*allu)#affichage des allumettes
                print("Il reste ",nballu," allumettes")
        print("il n'y a plus d'allumette")
        if numjoueur==1: #répartition des point si le joueur 1 a gagné
            scoreallumettej1.nbpoints=allj1+5
            scoreallumettej2.nbpoints=allj2-5
            print(pseudo1," a gagné")
        else : #répartition des point si le joueur 2 a gagné
            scoreallumettej1.nbpoints=allj1-5
            scoreallumettej2.nbpoints=allj2+5   
            print(pseudo2," a gagné")   
        scoreallumettej1.pseudo=pseudo1
        scoreallumettej2.pseudo=pseudo2
        ajoutscore(jeux,scoreallumettej1)
        ajoutscore(jeux,scoreallumettej2)
    elif saisie == '2' : 
        print("")
        print("")
        print("choisissez le niveau de difficulté :")
        print("1 - Facile")
        print("2 - Moyen")
        print("3 - Difficile")
        print("4 - Impossible")
        saisie=input("Faites votre choix :")
        while saisie!='1' and saisie!='2' and saisie!='3' and saisie!='4':
            print("erreur choix non valide")
            print("")
            print("")
            print("choisissez le niveau de difficulté :")
            print("1 - Facile")
            print("2 - Moyen")
            print("3 - Difficile")
            print("4 - Impossible")
            saisie=input("Faites votre choix :")
        if saisie=='1':
            pseudo1=choixpseudo(numjoueur)
            
            pseudo2="Bot 1"
            print("Il reste ",nballu," allumettes")
            while nballu>0 :# test si il reste des allumettes
                print(pseudo1," - Combien voulez vous enlever d'allumettes (1,2 ou 3) : ") #saisie du joueur 1
                saisie=input()
                    
                while est1nombre(saisie)==False or (int(saisie)!=1 and int(saisie)!=2 and int(saisie)!=3) or int(saisie)>nballu: #test si la saisie est valide pour le joueur 1
                    print("Erreur ce n'est pas un nombre possible d'allumettes restantes(1,2 ou 3) ")
                    print(pseudo1," - Combien voulez vous enlever d'allumettes (1,2 ou 3) : ")
                    saisie=input()
                choix=int(saisie)
                allj1=allj1 + choix
                nballu=enlevéallumette(nballu ,choix)
             
                print(nballu*allu)
                print("Il reste ",nballu," allumettes")
                if nballu>=0:
                    numjoueur = 2 
                if nballu>0 :# test si il reste des allumettes   
                    print("tour de l'ordinateur")
                    choixIA=randint(1,3)
                    while choixIA>nballu:
                        choixIA=randint(1,3)
                    print("l'ordinateur enlève",choixIA,"allumettes")
                    allj2=allj2 + choixIA
                    nballu=enlevéallumette(nballu ,choixIA)
                    print(nballu*allu)#affichage des allumettes
                    print("Il reste ",nballu," allumettes")
                    if nballu>=0:
                        numjoueur = 1
        elif saisie=='2':
            pseudo1=choixpseudo(numjoueur)
            pseudo2="Bot 1"
            print("Il reste ",nballu," allumettes")
            while nballu>0 :# test si il reste des allumettes
                numjoueur=1
                print(pseudo1," - Combien voulez vous enlever d'allumettes (1,2 ou 3) : ") #saisie du joueur 1
                saisie=input()
                    
                while est1nombre(saisie)==False or (int(saisie)!=1 and int(saisie)!=2 and int(saisie)!=3) or int(saisie)>nballu: #test si la saisie est valide pour le joueur 1
                    print("Erreur ce n'est pas un nombre possible d'allumettes restantes(1,2 ou 3) ")
                    print(pseudo1," - Combien voulez vous enlever d'allumettes (1,2 ou 3) : ")
                    saisie=input()
                choix=int(saisie)
                allj1=allj1 + choix
                nballu=enlevéallumette(nballu ,choix)
                        
                print(nballu*allu)
                print("Il reste ",nballu," allumettes")
                if nballu>=0:
                    numjoueur = 2
                if nballu>0 :# test si il reste des allumettes  
                    print("tour de l'ordinateur")
                    choixIA=randint(1,3)                  
                    if nballu==2:
                        choixIA=1
                    if nballu==3:
                        choixIA=2
                    if nballu==4:
                        choixIA=3
                    if nballu==6:
                        choixIA=1
                    if nballu==7:
                        choixIA=2
                    if nballu==8:
                        choixIA=3                      
                    while choixIA>nballu:
                        choixIA=randint(1,3)
                    print("l'ordinateur enlève",choixIA,"allumettes")
                    allj2=allj2 + choixIA
                    nballu=enlevéallumette(nballu ,choixIA)
                    print(nballu*allu)#affichage des allumettes
                    print("Il reste ",nballu," allumettes")
                    if nballu>=0:
                        numjoueur = 1
        elif saisie=='3':
            pseudo1=choixpseudo(numjoueur)
            numjoueur=1
            pseudo2="Bot 1"
            print("Il reste ",nballu," allumettes")
            while nballu>0 :# test si il reste des allumettes
                numjoueur=1
                print(pseudo1," - Combien voulez vous enlever d'allumettes (1,2 ou 3) : ") #saisie du joueur 1
                saisie=input()
                    
                while est1nombre(saisie)==False or (int(saisie)!=1 and int(saisie)!=2 and int(saisie)!=3) or int(saisie)>nballu: #test si la saisie est valide pour le joueur 1
                    print("Erreur ce n'est pas un nombre possible d'allumettes restantes(1,2 ou 3) ")
                    print(pseudo1," - Combien voulez vous enlever d'allumettes (1,2 ou 3) : ")
                    saisie=input()
                choix=int(saisie)
                allj1=allj1 + choix
                nballu=enlevéallumette(nballu ,choix)
                if nballu>=0:
                    numjoueur = 2
                if nballu>0:    
                    print(nballu*allu)
                    print("Il reste ",nballu," allumettes")
                    if nballu>0 :# test si il reste des allumettes                        
                        print("tour de l'ordinateur") 
                        if nballu%4==0:
                            choixIA=3
                        elif nballu%4==1:
                            choixIA=randint(1,3)
                            while nballu<choixIA:
                                choixIA=randint(1,3)                     
                        elif nballu%4==2:
                            choixIA=1
                        elif nballu%4==3:
                            choixIA=2                        
                        print("l'ordinateur enlève",choixIA,"allumettes")
                        allj2=allj2 + choixIA
                        nballu=enlevéallumette(nballu ,choixIA)  
                        print(nballu*allu)   
                        print("Il reste ",nballu," allumettes")
                        if nballu>=0:
                            numjoueur = 1
        elif saisie=='4':
            pseudo1="Bot 1"
            pseudo2=choixpseudo(numjoueur)
            print("Il reste ",nballu," allumettes")
            while nballu>0 :# test si il reste des allumettes
                numjoueur=1
                print("tour de l'ordinateur") 
                if nballu%4==0:
                    choixIA=3
                if nballu%4==1:
                    choixIA=randint(1,3)
                    while nballu<choixIA:
                        choixIA=randint(1,3) 
                if nballu%4==2:
                    choixIA=1
                if nballu%4==3:
                    choixIA=2                        
                print("l'ordinateur enlève",choixIA,"allumettes")
                allj2=allj2 + choixIA
                nballu=enlevéallumette(nballu ,choixIA)  
                print(nballu*allu)   
                print("Il reste ",nballu," allumettes")
                if nballu>=0:
                    numjoueur = 2
                if nballu>0:        
                    print(pseudo1," - Combien voulez vous enlever d'allumettes (1,2 ou 3) : ") #saisie du joueur 1
                    saisie=input()
                    
                    while est1nombre(saisie)==False or (int(saisie)!=1 and int(saisie)!=2 and int(saisie)!=3) or int(saisie)>nballu: #test si la saisie est valide pour le joueur 1
                        print("Erreur ce n'est pas un nombre possible d'allumettes restantes(1,2 ou 3) ")
                        print(pseudo1," - Combien voulez vous enlever d'allumettes (1,2 ou 3) : ")
                        saisie=input()
                    choix=int(saisie)
                    allj1=allj1 + choix
                    nballu=enlevéallumette(nballu ,choix)
                    if nballu>=0:
                        numjoueur = 1
        
    elif saisie == '3' :
            numjoueur=1
            pseudo1="Bot 1"
            numjoueur=2
            pseudo2="Bot 2"
            print(nballu*allu)
            print("Il reste ",nballu," allumettes")
            while nballu>0:
                numjoueur = 1 
                print("tour de l'ordinateur1")
                choixIA=randint(1,3)
                while choixIA>nballu:
                    choixIA=randint(1,3)
                sleep(1)
                print("l'ordinateur1 enlève ",choixIA," allumettes")
                allj2=allj2 + choixIA
                nballu=enlevéallumette(nballu ,choixIA)
                print(nballu*allu)#affichage des allumettes
                print("Il reste ",nballu," allumettes")
                if nballu>=0:
                    numjoueur = 2
                sleep(1)
                if nballu>0 :# test si il reste des allumettes   
                    print("tour de l'ordinateur2")
                    choixIA=randint(1,3)
                    while choixIA>nballu:
                        choixIA=randint(1,3)
                    print("l'ordinateur2 enlève",choixIA,"allumettes")
                    allj2=allj2 + choixIA
                    nballu=enlevéallumette(nballu ,choixIA)
                    print(nballu*allu)#affichage des allumettes
                    print("Il reste ",nballu," allumettes")
                    if nballu>=0:
                        numjoueur = 1
    if numjoueur==1: #répartition des point si le joueur 1 a gagné
        scoreallumettej1.nbpoints=allj1+5
        scoreallumettej2.nbpoints=allj2-5
        print(pseudo1," a gagné")
    else : #répartition des point si le joueur 2 a gagné
        scoreallumettej1.nbpoints=allj1-5
        scoreallumettej2.nbpoints=allj2+5   
        print(pseudo2," a gagné")   
    scoreallumettej1.pseudo=pseudo1
    scoreallumettej2.pseudo=pseudo2
    ajoutscore(jeux,scoreallumettej1)
    ajoutscore(jeux,scoreallumettej2)

     