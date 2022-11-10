# Debut

# on admet la fonction randint() qui renvoie une valeur comprise entre deux entiers.
# on admet la fonction input() qui renvoie la valeur donné par l'utilisateur.

# definir une fonction pfc() qui lance une partie de pierre feuille ciseau.
    # initialiser scoreJoueur et scoreIA, les variables de score des deux joueurs avec la valeur 0.
    # tant que scoreJoueur est different de 3 ou scoreIA est different de 3.
        # assigner à la variable choixJoueur la valeur du retour de la fonction input("choisissez une action : 1 pour feuille, 2 pour pierre, 3 pour ciseau").
        # assigner à la variable choixIA la valeur du retour de la fonction randint() avec comme parametres 1 et 3.

        # si choixJoueur est égal choixIA.
            # alors on écrit "égalité"

        # sinon si choixJoueur égal 1 et choixIA égal 2 ou choixJoueur égal 2 et choixIA égal 3
            # alors on écrit "victoire"
            # alors on incrémente scoreJoueur

        # sinon si choixJoueur égal 2 et choixIA égal 1 ou choixJoueur égal 3 et choixIA égal 2
            # alors on écrit "défaite"
            # alors on incrémente scoreIA

        # on écrit "scores : {scoreJoueur} / {scoreIA}"

    # si scoreJoueur est supérieur à scoreIA
        # alors écrire "vous avez gagné"

    # sinon
        # écrire "vous avez perdu"

# Fin