# Debut

# on admet la fonction randint() qui renvoie une valeur comprise entre deux entiers donné en parametre.
from random import randint
# on admet la fonction input() qui renvoie la valeur donné par l'utilisateur.

# definir une fonction pfc() qui lance une partie de pierre feuille ciseau.
def pfc():
    # définir scoreJoueur avec la valeur 0.
    scoreJoueur = 0
    # définir scoreIA avec la valeur 0.
    scoreIA = 0
    # tant que scoreJoueur est different de 3 ou scoreIA est different de 3.
    while scoreJoueur != 3 and scoreIA != 3:
        # assigner à la variable choixJoueur la valeur du retour de l'execution de la fonction input("choisissez une action : 1 pour feuille, 2 pour pierre, 3 pour ciseau").
        choixJoueur = int(input("choisissez une action : 1 pour feuille, 2 pour pierre, 3 pour ciseau : "))
        if choixJoueur not in [1,2,3]:
            print("lis les regles")
            pass
        # assigner à la variable choixIA la valeur du retour de l'execution de la fonction randint() avec comme parametres 1 et 3.
        choixIA = int(randint(1, 3))

        # si choixJoueur est égal choixIA.
        if choixJoueur == choixIA:
            # alors on écrit "égalité"
            print("égalité...")

        # sinon si choixJoueur égal 1 et choixIA égal 2 ou choixJoueur égal 2 et choixIA égal 3
        elif (choixJoueur == 1 and choixIA == 2) or (choixJoueur == 2 and choixIA == 3) or (choixJoueur == 3 and choixIA == 1):
            # alors on écrit "victoire"
            print("victoire!")
            # alors on incrémente scoreJoueur de 1
            scoreJoueur += 1

        # sinon si choixJoueur égal 2 et choixIA égal 1 ou choixJoueur égal 3 et choixIA égal 2
        elif (choixJoueur == 2 and choixIA == 1) or (choixJoueur == 3 and choixIA == 2) or (choixJoueur == 1 and choixIA == 3):
            # alors on écrit "défaite"
            print("défaite! nulos")
            # alors on incrémente scoreIA de 1
            scoreIA += 1

        # on écrit "scores : {scoreJoueur} / {scoreIA}"
        print(f"scores : {scoreJoueur} / {scoreIA}")

    # si scoreJoueur est supérieur à scoreIA
    if scoreJoueur > scoreIA:
        # alors écrire "vous avez gagné"
        print("vous avez gagné")

    # sinon
    else:
        # écrire "vous avez perdu"
        print("vous avez perdu")

# Fin

pfc()