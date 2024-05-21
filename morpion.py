#programme morpion
from __future__ import annotations
from gestionscore import *
from fonction import *
from time import *
import random

def morpion(x : str, y : str,val : list[list[str]],tour : int,pseudo : str )->list[list[str]]:
    """
    Test si la saisie colonne ou la ligne et valide ou déjà occupé est impléente la liste vec le choix du joueur .
    entrée :
        x(str) : indice de la ligne du morpion entre 0 et 2
        y(str) : indice de la colonne du morpion entre 0 et 2
    sortie : la liste modifier avec un rond ou un carré a l'indice choisit
    """
    while not est1nombre(str(x)) or not est1nombre(str(y)): #validité du choix du joueur
        print("Numéro de ligne ou de colonne non valide ou case déjà occupé.")   
        print(pseudo," : choisissez le numéro de la ligne ")
        x=input()
        print(pseudo," : choisissez le numéro de la colonne : ")
        y=input()
    while int(x)<0 or int(x)>2 or int(y)<0 or int(y)>2 or val[int(x)][int(y)]!=' ':
        print("Numéro de ligne ou de colonne non valide ou case déjà occupé.")
        print(pseudo," : choisissez le numéro de la ligne ")
        x=input()
        print(pseudo," : choisissez le numéro de la colonne : ")
        y=input()
    
    if tour%2==0 : #implémentation de la valeur dans la liste
        val[int(x)][int(y)]='X'
    else:
        val[int(x)][int(y)]='O'
    return val

def morpionbot(x : str, y : str,val : list[list[str]],tour : int,pseudo : str )->list[list[str]]:
    """
    Test si la saisie colonne ou la ligne et valide ou déjà occupé est implémente la liste avec le choix du joueur .
    entrée :
        x(str) : indice de la ligne du morpion entre 0 et 2
        y(str) : indice de la colonne du morpion entre 0 et 2
    sortie : la liste modifier avec un rond ou un carré a l'indice choisit
    """
    while not est1nombre(str(x)) or not est1nombre(str(y)): #validité du choix du joueur
        x=str(random.randint(0, 2))
        y=str(random.randint(0, 2))
    while int(x)<0 or int(x)>2 or int(y)<0 or int(y)>2 or val[int(x)][int(y)]!=' ':
        x=str(random.randint(0, 2))
        y=str(random.randint(0, 2))
    
    if tour%2==0 : #implémentation de la valeur dans la liste
        val[int(x)][int(y)]='X'
    else:
        val[int(x)][int(y)]='O'
    return val

def verif_menace(val, signe1, signe2):
    """Fonction qui cherche selon un certain ordre de priorité quelle case menace le plus le joueur.
    Entrée : Le signe du joueur dont on doit analyser les coups
    Sortie : Un tuple d'entiers correspondant à la case la plus menaçante pour l'autre joueur."""
    for i in range(3):
        # Vérification des menaces sur les lignes
        if val[i].count(signe1) == 2 and val[i].count(' ') == 1:
            return i, val[i].index(' ')
        # Vérification des menaces sur les colonnes
        if [val[j][i] for j in range(3)].count(signe1) == 2 and [val[j][i] for j in range(3)].count(' ') == 1:
            return [val[j][i] for j in range(3)].index(' '), i
    # Vérification des menaces sur les diagonales
    if val[0][0] == val[1][1] == signe1 and val[2][2] == ' ':
        return 2, 2
    if val[0][2] == val[1][1] == signe1 and val[2][0] == ' ':
        return 2, 0
    if val[2][0] == val[1][1] == signe1 and val[0][2] == ' ':
        return 0, 2
    if val[2][2] == val[1][1] == signe1 and val[0][0] == ' ':
        return 0, 0
    return None


    

def test(val : list[list[str]])->bool:
    """
    Test si un des deux joueur a gagné .
    entrée : le tableau de morpion
    sortie : un booléen qui vaut vraie si le joueur a gagné
    """
    i : int
    j : int
    victoire : bool
    victoire=False
    for i in range(0,2):
        if val[i][0]==val[i][1] and val[i][1]==val[i][2] and val[i][0]!=' ':
            victoire=True
        if val[0][i]==val[1][i] and val[1][i]==val[2][i] and val[0][i]!=' ':
            victoire=True
    if val[0][0]==val[1][1] and val[1][1]==val[2][2] and val[0][0]!=' ':
        victoire=True
    if val[2][0]==val[1][1] and val[1][1]==val[0][2] and val[2][0]!=' ':
        victoire=True
    return victoire


def testegalite(val : list[list[str]])->bool:
    """
    Test si il y a égalité .
    entrée : le tableau du morpion
    sortie : un booléen qui vaut True si égalité
    """
    nul : bool
    nul = False
    if val[0][0]!=' ' and val[0][1]!=' ' and val[0][2]!=' ' and val[1][0]!=' ' and val[2][0]!=' ' and val[1][1]!=' ' and val[2][1]!=' ' and val[1][2]!=' ' and val[2][2]!=' ' :
        nul = True
    return nul

def botfacile() :
    """Procédure qui fait jouer l'utilisateur contre un ordinateur de difficulté facile.
    Entrée : Rien
    Sortie : Rien (procédure)
    """
    scoremorpionj1 : score
    scoremorpionj2 : score
    scoremorpionj1 = score()
    scoremorpionj2 = score()
    print("Joueur contre ordinateur (Difficulté Facile)")
    partiegagnée=False
    #saisie du nom des joueurs et test de leurs validité
    jeux='morpion'
    numjoueur=1
    pseudo1=choixpseudo(numjoueur)
    numjoueur=2
    pseudo2 = "Bot 1"
    while not testpseudo(pseudo1,pseudo2):
        numjoueur = 1
        pseudo1 = choixpseudo(numjoueur)
        numjoueur = 2
        pseudo2 = "Bot 1"
    #fin de la saisie
    val=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    tour=0
    print("    0   1   2  ")
    print("  -------------")
    print("0 |   |   |   |")
    print("  -------------")
    print("1 |   |   |   |")
    print("  -------------")
    print("2 |   |   |   |")
    print("  -------------")
    
    while partiegagnée==False and not testegalite(val):#test si la partie et terminer
        if tour%2==0 : #tour du premier joueur
            print(pseudo1," : choisissez le numéro de la ligne : ")
            x = input()
            print(pseudo1," : choisissez le numéro de la colonne : ")
            y = input()
            val = morpion(x,y,val,tour,pseudo1)
            print("    0   1   2  ")
            print("  -------------")
            print("0 |",val[0][0],"|",val[0][1],"|",val[0][2],"|")
            print("  -------------")
            print("1 |",val[1][0],"|",val[1][1],"|",val[1][2],"|")
            print("  -------------")
            print("2 |",val[2][0],"|",val[2][1],"|",val[2][2],"|")
            print("  -------------")
            tour=tour+1
            partiegagnée=test(val)
        elif tour%2==1 : #tour du deuxième joueur
            print(pseudo2," : choisissez le numéro de la ligne ")
            x = str(random.randint(0, 2))
            print(pseudo2," : choisissez le numéro de la colonne : ")
            y = str(random.randint(0, 2))
            val = morpionbot(x,y,val,tour,pseudo2)
            print("    0   1   2  ")
            print("  -------------")
            print("0 |",val[0][0],"|",val[0][1],"|",val[0][2],"|")
            print("  -------------")
            print("1 |",val[1][0],"|",val[1][1],"|",val[1][2],"|")
            print("  -------------")
            print("2 |",val[2][0],"|",val[2][1],"|",val[2][2],"|")
            print("  -------------")
            tour = tour+1
            partiegagnée = test(val)
        if partiegagnée == True: #test si un des joueur a gagner
            print("Partie fini")
            if tour%2==0 : #point des joueur si joueur 2 a gagné
                print(pseudo2," à gagné")
                scoremorpionj1.nbpoints=0
                scoremorpionj2.nbpoints=5                
            else : #point des joueur si joueur 1 a gagné
                print(pseudo1," à gagné")
                scoremorpionj1.nbpoints=5
                scoremorpionj2.nbpoints=0
        elif testegalite(val):#test si égalité
            print("Partie fini")
            print("Match nul")
            scoremorpionj1.nbpoints=2  #point des joueur si égalité
            scoremorpionj2.nbpoints=2  #point des joueur si égalité
        scoremorpionj1.pseudo=pseudo1
        scoremorpionj2.pseudo=pseudo2
    ajoutscore(jeux,scoremorpionj1)
    ajoutscore(jeux,scoremorpionj2)

def botmoyen() :
    """Procédure qui fait jouer l'utilisateur contre un ordinateur de difficulté moyen.
    Entrée : Rien
    Sortie : Rien (procédure)
    """
    pos_menace : tuple
    scoremorpionj1 = score()
    scoremorpionj2 = score()
    print("Joueur contre ordinateur (Difficulté Moyenne)")
    partiegagnee = False
    jeux = 'morpion'
    numjoueur = 1
    pseudo1 = choixpseudo(numjoueur)
    pseudo2 = "Bot Moyen"
    while not testpseudo(pseudo1, pseudo2):
        numjoueur = 1
        pseudo1 = choixpseudo(numjoueur)
        numjoueur = 2
        pseudo2 = "Bot Moyen"

    val = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    tour = 0

    print("    0   1   2  ")
    print("  -------------")
    print("0 |   |   |   |")
    print("  -------------")
    print("1 |   |   |   |")
    print("  -------------")
    print("2 |   |   |   |")
    print("  -------------")

    while not partiegagnee and not testegalite(val):
        if tour % 2 == 0:  # Tour du joueur
            print(pseudo1, " : choisissez le numéro de la ligne : ")
            x = input()
            print(pseudo1, " : choisissez le numéro de la colonne : ")
            y = input()
            val = morpion(x, y, val, tour, pseudo1)

        elif tour % 2 == 1:  # Tour du bot moyen
            pos_menace = verif_menace(val, 'X', 'O')
            if pos_menace is not None:
                x, y = pos_menace
            else:
                x, y = str(random.randint(0, 2)), str(random.randint(0, 2))
            val = morpionbot(x, y, val, tour, pseudo2)

        # Affichage du tableau
        print("    0   1   2  ")
        print("  -------------")
        print("0 |", val[0][0], "|", val[0][1], "|", val[0][2], "|")
        print("  -------------")
        print("1 |", val[1][0], "|", val[1][1], "|", val[1][2], "|")
        print("  -------------")
        print("2 |", val[2][0], "|", val[2][1], "|", val[2][2], "|")
        print("  -------------")

        tour += 1
        partiegagnee = test(val)

    print("Partie finie")

    if partiegagnee:
        if tour % 2 == 0:
            print(pseudo2, " a gagné")
            scoremorpionj1.nbpoints = 5
            scoremorpionj2.nbpoints = 0
        else:
            print(pseudo1, " a gagné")
            scoremorpionj1.nbpoints = 0
            scoremorpionj2.nbpoints = 5
    else:
        print("Match nul")
        scoremorpionj1.nbpoints = 2
        scoremorpionj2.nbpoints = 2

    scoremorpionj1.pseudo = pseudo1
    scoremorpionj2.pseudo = pseudo2

    ajoutscore(jeux, scoremorpionj1)
    ajoutscore(jeux, scoremorpionj2)



def jeumorpion():
    """
    Procédure principale du jeu du morpion
    """
    x : str #valeur en ligne
    y : str #vleur en colonne
    pseudo1 : str
    pseudo2 : str
    tour : int #nombre de tour
    saisie : str
    partiegagnée : bool
    scoremorpionj1 : score
    scoremorpionj2 : score    
    scoremorpionj1=score()
    scoremorpionj2=score()
    choixdif : str
    val : list[list[str]] #tableau du morpion
    print(
"""
+=======================================+
| __  __                  _             |
||  \/  | ___  _ __ _ __ (_) ___  _ __  |
|| |\/| |/ _ \| '__| '_ \| |/ _ \| '_ \ |
|| |  | | (_) | |  | |_) | | (_) | | | ||
||_|  |_|\___/|_|  | .__/|_|\___/|_| |_||
|                  |_|                  |
+=======================================+
"""
    )
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
        print("Joueur contre joueur")
        partiegagnée=False
        #saisie du nom des joueurs et test de leurs validité
        jeux='morpion'
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
        val=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        tour=0
        print("    0   1   2  ")
        print("  -------------")
        print("0 |   |   |   |")
        print("  -------------")
        print("1 |   |   |   |")
        print("  -------------")
        print("2 |   |   |   |")
        print("  -------------")
        
        while partiegagnée==False and not testegalite(val):#test si la partie et terminer
            if tour%2==0 : #tour du premier joueur
                print(pseudo1," : choisissez le numéro de la ligne ")
                x=input()
                print(pseudo1," : choisissez le numéro de la colonne : ")
                y=input()
                val=morpion(x,y,val,tour,pseudo1)
                print("    0   1   2  ")
                print("  -------------")
                print("0 |",val[0][0],"|",val[0][1],"|",val[0][2],"|")
                print("  -------------")
                print("1 |",val[1][0],"|",val[1][1],"|",val[1][2],"|")
                print("  -------------")
                print("2 |",val[2][0],"|",val[2][1],"|",val[2][2],"|")
                print("  -------------")
                tour=tour+1
                partiegagnée=test(val)
            elif tour%2==1 : #tour du deuxième joueur
                print(pseudo2," : choisissez le numéro de la ligne ")
                x=input()
                print(pseudo2," : choisissez le numéro de la colonne : ")
                y=input()
                val=morpion(x,y,val,tour,pseudo2)
                print("    0   1   2  ")
                print("  -------------")
                print("0 |",val[0][0],"|",val[0][1],"|",val[0][2],"|")
                print("  -------------")
                print("1 |",val[1][0],"|",val[1][1],"|",val[1][2],"|")
                print("  -------------")
                print("2 |",val[2][0],"|",val[2][1],"|",val[2][2],"|")
                print("  -------------")
                tour=tour+1
                partiegagnée=test(val)
            if partiegagnée==True: #test si un des joueur a gagner
                print("Partie fini")
                if tour%2==0 : #point des joueur si joueur 2 a gagné
                    print(pseudo2," à gagné")
                    scoremorpionj1.nbpoints=0
                    scoremorpionj2.nbpoints=5                
                else : #point des joueur si joueur 1 a gagné
                    print(pseudo1," à gagné")
                    scoremorpionj1.nbpoints=5
                    scoremorpionj2.nbpoints=0
            elif testegalite(val):#test si égalité
                print("Partie fini")
                print("Match nul")
                scoremorpionj1.nbpoints=2  #point des joueur si égalité
                scoremorpionj2.nbpoints=2  #point des joueur si égalité
            scoremorpionj1.pseudo=pseudo1
            scoremorpionj2.pseudo=pseudo2
        ajoutscore(jeux,scoremorpionj1)
        ajoutscore(jeux,scoremorpionj2)
    elif saisie == '2' :
        print("1 - Facile")
        print("2 - Moyen")
        choixdif = input("Choisissez votre difficulté !")
        while choixdif!='1' and choixdif!='2' : 
            choixdif = input("Erreur, choisissez votre difficulté !")
        if choixdif == '1' :
            botfacile()
        elif choixdif == '2' :
            botmoyen()
    elif saisie == '3' :
        print("Ordinateur contre ordinateur")
        partiegagnée=False
        #saisie du nom des joueurs et test de leurs validité
        jeux='morpion'
        numjoueur=1
        pseudo1="Bot 1"
        numjoueur=2
        pseudo2 = "Bot 2"
        while not testpseudo(pseudo1,pseudo2):
            numjoueur = 1
            pseudo1 = choixpseudo(numjoueur)
            numjoueur = 2
            pseudo2 = "Bot 1"
        #fin de la saisie
        val=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        tour=0
        print("    0   1   2  ")
        print("  -------------")
        print("0 |   |   |   |")
        print("  -------------")
        print("1 |   |   |   |")
        print("  -------------")
        print("2 |   |   |   |")
        print("  -------------")
        
        while partiegagnée==False and not testegalite(val):#test si la partie et terminer
            if tour%2==0 : #tour du premier joueur
                print(pseudo1," : choisissez le numéro de la ligne : ")
                x = str(random.randint(0, 2))
                print(pseudo1," : choisissez le numéro de la colonne : ")
                y = str(random.randint(0, 2))
                val = morpionbot(x,y,val,tour,pseudo1)
                sleep(1)
                print("    0   1   2  ")
                print("  -------------")
                print("0 |",val[0][0],"|",val[0][1],"|",val[0][2],"|")
                print("  -------------")
                print("1 |",val[1][0],"|",val[1][1],"|",val[1][2],"|")
                print("  -------------")
                print("2 |",val[2][0],"|",val[2][1],"|",val[2][2],"|")
                print("  -------------")
                tour=tour+1
                partiegagnée=test(val)
            elif tour%2==1 : #tour du deuxième joueur
                print(pseudo2," : choisissez le numéro de la ligne ")
                x = str(random.randint(0, 2))
                print(pseudo2," : choisissez le numéro de la colonne : ")
                y = str(random.randint(0, 2))
                val = morpionbot(x,y,val,tour,pseudo2)
                sleep(1)
                print("    0   1   2  ")
                print("  -------------")
                print("0 |",val[0][0],"|",val[0][1],"|",val[0][2],"|")
                print("  -------------")
                print("1 |",val[1][0],"|",val[1][1],"|",val[1][2],"|")
                print("  -------------")
                print("2 |",val[2][0],"|",val[2][1],"|",val[2][2],"|")
                print("  -------------")
                tour = tour+1
                partiegagnée = test(val)
            if partiegagnée == True: #test si un des joueur a gagner
                print("Partie fini")
                if tour%2==0 : #point des joueur si joueur 2 a gagné
                    print(pseudo2," à gagné")
                    scoremorpionj1.nbpoints=0
                    scoremorpionj2.nbpoints=5                
                else : #point des joueur si joueur 1 a gagné
                    print(pseudo1," à gagné")
                    scoremorpionj1.nbpoints=5
                    scoremorpionj2.nbpoints=0
            elif testegalite(val):#test si égalité
                print("Partie fini")
                print("Match nul")
                scoremorpionj1.nbpoints=2  #point des joueur si égalité
                scoremorpionj2.nbpoints=2  #point des joueur si égalité
            scoremorpionj1.pseudo=pseudo1
            scoremorpionj2.pseudo=pseudo2
        ajoutscore(jeux,scoremorpionj1)
        ajoutscore(jeux,scoremorpionj2)
    elif saisie == '4' :
        print("Vous avez quitté.")

