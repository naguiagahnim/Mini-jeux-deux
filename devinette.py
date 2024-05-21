# programme devinette
from __future__ import annotations
from gestionscore import *
from fonction import *
from getpass import *
from random import *
from time import *

def saisielim(pseudo : str)->str :
    saisie : str #choix du joueur en chaine de caractère
    print(pseudo," saisissez le nombre limite (entier supérieur à 1):") #saisie de la limite
    saisie=input()
    while est1nombre(saisie)==False : #test de validité de la saisie de la limite
        print("Erreur ce n'est pas un nombre entier supérieur à 1 .")
        print(pseudo," saisissez le nombre limite :")
        saisie=input()
    while int(saisie)<=1:
        print("Erreur ce n'est pas un nombre entier supérieur à 1 .")
        print(pseudo," saisissez le nombre limite :")
        saisie=input()
        while est1nombre(saisie)==False : #test de validité de la saisie de la limite
            print("Erreur ce n'est pas un nombre entier supérieur à 1 .")
            print(pseudo," saisissez le nombre limite :")
            saisie=input()
    return saisie

def saisienb(pseudo : str,lim : int)->str :
    saisie : str #choix du joueur en chaine de caractère
    saisie=getpass(prompt='nombre à deviner : ', stream=None) #saisie du nombre a deviner
    while est1nombre(saisie)==False : #test de validité de la saisie du nombre à deviner
        print("Erreur ce n'est pas un nombre entier positif.")
        saisie=getpass(prompt='nombre à deviner : ', stream=None)
    while int(saisie)<1 or int(saisie)>lim:
        print("Erreur ce n'est pas un nombre entier supérieur à 0 ou le nombre est supérieur à la limite .")
        saisie=getpass(prompt='nombre à deviner : ', stream=None)
        while est1nombre(saisie)==False :
            print("Erreur ce n'est pas un nombre entier positif.")
            saisie=getpass(prompt='nombre à deviner : ', stream=None)
    #fin du test de validité de la saisie du nombre à deviner
    return saisie

def saisiessai(pseudo : str, lim : int)->str :    
    saisie : str #choix du joueur en chaine de caractère
    print(pseudo," essayez de deviner le nombre :")
    saisie=input()
    while est1nombre(saisie)==False :
        print("Erreur ce n'est pas un nombre entier positif.")
        print(pseudo," essayez de deviner le nombre :")
        saisie=input()
    while int(saisie)<1 or int(saisie)>lim:
        print("Erreur ce n'est pas un nombre entier supérieur à 0 ou le nombre est supérieur à la limite.")
        print(pseudo," essayez de deviner le nombre :")
        saisie=input()
        while est1nombre(saisie)==False :
            print("Erreur ce n'est pas un nombre entier positif.")
            print(pseudo," essayez de deviner le nombre :")
            saisie=input()
    #fin du test
    return saisie

def reponse(pseudo : str,n : int , essai : int)->str:
    choix : int
    #saisie de la réponse de l'autre joueur par rapport a l'essaie si la réponse n'est pas bonne refait la saisie
    print(pseudo," : 1 - le nombre est trop grand.")
    print("2 - le nombre est trop petit.")
    print("3 - le nombre est le bon. Bravo !")
    print(pseudo," faites votre choix (1,2 ou 3) :")
    saisie=input()

    #test si le choix est possible
    while est1nombre(saisie)==False or (int(saisie)!=1 and int(saisie)!=2 and int(saisie)!=3):
        print("Erreur ce n'est pas un choix possible.")
        print(pseudo, " faites votre choix (1,2 ou 3) :")
        saisie=input()
    choix=int(saisie)
        #fin du test

        #test si le joueur a donné la bonne réponse
    while (choix==1 and n>essai) or (choix==1 and n==essai) or (choix==2 and n<essai) or (choix==2 and n==essai) or (choix==3 and n<essai) or (choix==3 and n>essai) :
        print("Menteur !")
        print(pseudo," : 1 - le nombre est trop grand.")
        print("2 - le nombre est trop petit.")
        print("3 - le nombre est le bon. Bravo !")
        print(pseudo," faites votre choix (1,2 ou 3) :")
        saisie=input()
        #test si le choix est possible
        while est1nombre(saisie)==False or (int(saisie)!=1 and int(saisie)!=2 and int(saisie)!=3):
            print("Erreur ce n'est pas un nombre entier positif.")
            print(pseudo, " faites votre choix (1,2 ou 3) :")
            saisie=input()
        choix=int(saisie)
    choix=int(saisie)
    return choix
               
def devinnb():
    """
    Procédure principale du jeu devine nombre
    """
    n : int
    pseudo1 : str
    pseudo2 : str
    lim : int #la limite de nombre choisit par le joueur
    essai : int #essai du joueur pour trouvé le bon nombre
    choix : int #choix du joueur
    saisie : str #choix du joueur en chaine de caractère
    trouvé : bool #le joueur à trouvé le bon nombre
    scoredevinette : score
    nbessai : int #le nombre d'essaie du joueur
    jeux : str
    numjoueur : int
    max : int
    min : int
    print(
"""
+===========================================+
| ____             _            _   _       |
||  _ \  _____   _(_)_ __   ___| |_| |_ ___ |
|| | | |/ _ \ \ / / | '_ \ / _ \ __| __/ _ \|
|| |_| |  __/\ V /| | | | |  __/ |_| ||  __/|
||____/ \___| \_/ |_|_| |_|\___|\__|\__\___||
+===========================================+
"""
    )
    print("------------------------------------")
    print("|                                  |")
    print("| 1 - Jouer à 2 joueur             |")
    print("| 2 - Jouer contre l'ordinateur    |")
    print("| 3 - Ordinateur contre ordinateur |")
    print("| 4 - Quitter                      |")
    print("|                                  |")
    print("------------------------------------") 
    saisie=input("Faites votre choix :")
        #test si le choix est possible
    while est1nombre(saisie)==False or (int(saisie)!=1 and int(saisie)!=2 and int(saisie)!=3):
        saisie=input("Erreur ce n'est pas un choix possible. Faites votre choix (1,2 ou 3) :")        
    choix=int(saisie)
        #fin du test
    scoredevinette=score()
    trouvé = False
    nbessai=0
    jeux='devinette'
    if choix==1:
        #saisie du nom des joueurs et test de leurs validité    
        numjoueur=1
        pseudo1=choixpseudo(numjoueur)
        numjoueur=2
        pseudo2=choixpseudo(numjoueur)
        while not testpseudo(pseudo1,pseudo2):
            numjoueur=1
            pseudo1=choixpseudo(numjoueur)
            numjoueur=2
            pseudo2=choixpseudo(numjoueur)
        #fin de la saisie
        lim=int(saisielim(pseudo1))
        n=int(saisienb(pseudo1,lim))
        while trouvé==False : #test si le nombre saisie est égale au nombre cherché    
            essai=int(saisiessai(pseudo2,lim))
            nbessai=nbessai+1 #compte le nombre d'essaie pour le calcul du score
            choix=reponse(pseudo1, n, essai)
            #affichage du choix si il est valide
            if choix==1 and n<essai :
                print("trop grand")
            elif choix==2 and n>essai :
                print("trop petit")
            elif choix==3 and n==essai :
                print("c'est gagné")
                trouvé=True     
        scoredevinette.pseudo=pseudo2
        scoredevinette.nbpoints=int(lim/nbessai)#calcul du score du gagnant
        ajoutscore(jeux,scoredevinette)
    elif choix==2: 
        print("")
        print("")
        print("---------------------------------")
        print("|                               |")
        print("| 1 - L'ordinateur devine       |")
        print("| 2 - L'ordinateur fait deviner |")
        print("| 3 - Quitter                   |")
        print("|                               |") 
        print("---------------------------------") 
        saisie=input("Faites votre choix :")
        #test si le choix est possible
        while est1nombre(saisie)==False or (int(saisie)!=1 and int(saisie)!=2 and int(saisie)!=3):
            saisie=input("Erreur ce n'est pas un choix possible. Faites votre choix (1,2 ou 3) :")        
        choix=int(saisie)
        #fin du test
        if choix==1:
            print("")
            print("")
            print("choisissez le niveau de difficulté :")
            print("1 - Moyen")
            print("2 - Difficile")
            saisie=input("Faites votre choix :")
            #test si le choix est possible
            while est1nombre(saisie)==False or (int(saisie)!=1 and int(saisie)!=2 and int(saisie)!=3):
                saisie=input("Erreur ce n'est pas un choix possible. Faites votre choix (1,2 ou 3) :")        
            choix=int(saisie)
            #fin du test
            numjoueur=1
            pseudo1=choixpseudo(numjoueur)
            numjoueur=2
            pseudo2='Bot 1'
            while not testpseudo(pseudo1,pseudo2):
                numjoueur=1
                pseudo1='Bot 1'
                numjoueur=2
                pseudo2=choixpseudo(numjoueur)
                #fin de la saisie   
            lim=int(saisielim(pseudo1))
            n=int(saisienb(pseudo1,lim))
            min=0
            max=lim+1
            if choix==1:
                while trouvé==False :   
                    essai=randint(min+1,max-1)
                    print(pseudo2," essayez de deviner le nombre :")
                    print(essai)
                    nbessai=nbessai+1 #compte le nombre d'essaie pour le calcul du score
                    choix=reponse(pseudo1, n, essai)
                    if choix==1 and n<essai :
                        print("trop grand")
                        max=essai
                    elif choix==2 and n>essai :
                        print("trop petit")
                        min=essai
                    elif choix==3 and n==essai :
                        print("c'est gagné")
                        trouvé=True     
            if choix==2:
                 while trouvé==False :   
                    essai=int((min+max)/2)
                    print(pseudo2," essayez de deviner le nombre :")
                    print(essai)
                    nbessai=nbessai+1 #compte le nombre d'essaie pour le calcul du score
                    choix=reponse(pseudo1, n, essai)
                    if choix==1 and n<essai :
                        print("trop grand")
                        max=essai
                    elif choix==2 and n>essai :
                        print("trop petit")
                        min=essai
                    elif choix==3 and n==essai :
                        print("c'est gagné")
                        trouvé=True     

        elif choix==2:
            print("")
            print("")
            print("choisissez le niveau de difficulté :")
            print("1 - Facile")
            print("2 - Moyen")
            print("3 - Difficile")
            saisie=input("Faites votre choix :")
            #test si le choix est possible
            while est1nombre(saisie)==False or (int(saisie)!=1 and int(saisie)!=2 and int(saisie)!=3):
                saisie=input("Erreur ce n'est pas un choix possible. Faites votre choix (1,2 ou 3) :")        
            choix=int(saisie)
            #fin du test
            numjoueur=1
            pseudo1='Bot 1'
            numjoueur=2
            pseudo2=choixpseudo(numjoueur)
            while not testpseudo(pseudo1,pseudo2):
                numjoueur=1
                pseudo1='Bot 1'
                numjoueur=2
                pseudo2=choixpseudo(numjoueur)
                #fin de la saisie   
            if choix==1:
                lim=randint(2,50)
            if choix==2:
                lim=randint(50,500)
            if choix==3:
                lim=randint(500,10000)    
            print("Limite :",lim)
            n=randint(1,lim)
            while trouvé==False : #test si le nombre saisie est égale au nombre cherché    
                essai=int(saisiessai(pseudo2,lim))
                nbessai=nbessai+1 #compte le nombre d'essaie pour le calcul du score
                if n<essai :
                    print("trop grand")
                elif n>essai :
                    print("trop petit")
                elif n==essai :
                    print("c'est gagné")
                    trouvé=True     


    elif choix==3:
        pseudo1='Bot 2'
        pseudo2='Bot 1'
        lim=randint(2,500)
        n=randint(1,lim)
        print("la limite est ",lim)
        min=0
        max=lim+1
        while trouvé==False :   
            essai=randint(min+1,max-1)
            print(pseudo2," essayez de deviner le nombre :")
            print(essai)
            nbessai=nbessai+1
            if n<essai :
                print("trop grand")
                max=essai
            elif n>essai :
                print("trop petit")
                min=essai
            elif n==essai :
                print("c'est gagné")
                trouvé=True
            sleep(1)

    scoredevinette.pseudo=pseudo2
    scoredevinette.nbpoints=int(lim/nbessai)#calcul du score du gagnant
    ajoutscore(jeux,scoredevinette)    

        


                    
