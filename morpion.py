# on admet la fonction input() qui renvoie la valeur donné par l'utilisateur.
# on admet la fonction randint() qui renvoie une valeur comprise entre deux entiers donné en parametre.
from random import randint

# definir une fonction morpion() qui lance une partie de morpion entre deux joueurs.
def morpion():
    # definir un tableau de 3 x 3 avec des symboles vide.
    tab = [ ["_" for i in range(3)] for i in range(3) ]

    # définir bullet avec comme valeur 1
    bullet = 1

    # définir un dictionaire dans lequel on stock le nom des joueurs
    curPlayer = {
        1: "Joueur 1",
        -1: "Joueur 2"
    }
    # definir une variable à laquelle on assigne l'ID du joueur actuel
    curPlayerID = 1
    # definir un dictionaire dans lequel on stock le symbole de chaque joueur en fonction de son ID
    playerSymbole = {
        1: "O",
        -1: "X"
    }

    # tant que True
    while True:
        # définir la variable booléenne check à False
        check = False
        # tant que check n'est pas égal à True
        while not check:
            # écrire le nom du joueur dont c'est le tour en fonction de l'ID du joueur actuel dans curPlayer 
            print(f"{curPlayer[curPlayerID]}, c'est à toi !")

            # on assigne à la variable choixX le retour de la variable input("coordonné x : ") sous forme d'entier
            choixX = int(input("Ligne (1 à 3): "))
            # on assigne à la variable choixX le retour de la variable input("coordonné y : ") sous forme d'entier
            choixY = int(input("Colonne (1 à 3): "))

            # si choixX et choixY sont égal à -1 et que bullet égal 1
            if choixX == -1 and choixY == -1 and bullet == 1:
                # check égal True
                check = True
                x1=randint(0,2)
                y1=randint(0,2)
                x2=None
                y2=None
                while x1 != x2 and y1!= y2:
                    x2=randint(0,2)
                    y2=randint(0,2)
                print(x1, y1)
                print(x2, y2)
                tab[x1][y1] = playerSymbole[curPlayerID]
                tab[x2][y2] = playerSymbole[curPlayerID]
                curPlayerID = curPlayerID * -1
                bullet -= 1
            # sinon si choixX et choixY sont égal à -1 et que bullet n'est pas égal à 1
            elif choixX == -1 and choixY == -1 and bullet != 1:
                # alors on ecrit "à court de balle...".
                print("à court de balle...")

            # sinon si les valeurs de choixX et choixY ne sont pas dans le tableau ou que tab[choixX-1][choixY-1] est different de "_".
            elif not (choixX >= 1 and choixX <= 3 and choixY >= 1 and choixY <= 3) or  tab[choixX-1][choixY-1] != "_":
                # alors on ecrit "case occupée, fais un autre choix".
                print("Impossible, fais un autre choix")
            
            # sinon
            else:
                # assigner le symbole du joueur aux coordonnées choixX, choixY dans tab.
                tab[choixX-1][choixY-1] = playerSymbole[curPlayerID]
                check = True

        # pour chaque element de tab
        for i in tab:
            # on imrpime la ligne du tableau
            print(i)

        # on stock temporairement le symbole du joueur actuel dans la variable cur.
        cur = playerSymbole[curPlayerID]
        # si l'action du joueur est un action qui lui fait gagner la partie.
        if (tab[0][0] == cur and tab[0][1] == cur and tab[0][2] == cur) or (tab[1][0] == cur and tab[1][1] == cur and tab[1][2] == cur) or (tab[2][0] == cur and tab[2][1] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][0] == cur and tab[2][0] == cur) or (tab[0][1] == cur and tab[1][1] == cur and tab[2][1] == cur) or (tab[0][2] == cur and tab[1][2] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][1] == cur and tab[2][2] == cur) or (tab[0][2] == cur and tab[1][1] == cur and tab[2][0] == cur):
            # alors on ecrit quel joueur à gagné
            print(f"{curPlayer[curPlayerID]} a gagné")
            # puis on force la sortie de la boucle infinie avec un break
            break
        
        # si tab[choixX-1][choixY-1] est égal au symbole du joueur.
        if tab[choixX-1][choixY-1] == playerSymbole[curPlayerID]:
            # alors on change l'ID de curPlayerID en multipliant la variable par -1.
            curPlayerID = curPlayerID * -1

morpion()