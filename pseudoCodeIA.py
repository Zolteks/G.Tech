# on importe une class de copy car la copie de liste de fonctionne pas

# définir la fonction morpionImpossible() qui lance une partie de morpion ou l'IA gagne tout le temps ou fait une égalité.
    
    # initialise le tableau de jeu au format 3 x 3.
    
    # definir le dictionaire qui contient les noms des joueurs en fonction de leur ID.

    # initialise l'ID du joueur actuel à 1.

    # définir le dictionaire qui contient le symbole d'un joueur en fonction de son ID.

    # modifier le tableau d'après la première action de l'IA en modifiant tab[1][1]

    # initialise la variable du nombre d'action de la partie à 1.

    # tant que True
        # incrémenter action de 1
        
        # afficher le tableau de jeu

        # si curPlayerID égal
            # définir une variable booléenne à False
            # tant que choix n'est pas égal à True.
                # écrire "c'est à toi de jouer"
                # définir choixX avec le retour de la fonction input("Ligne (1 à 3): ")
                # définir choixX avec le retour de la fonction input("Colonne (1 à 3): ")
                # si tab[choixX][choixY] est égal à "_".
                    # alors, écrire "case occupée, fais un autre choix"
                # sinon
                    # assigner à tab[choixX][choixY] la valeur de playerSymbole[curPlayerID]
                    # assigner à choix la valeur True
        # sinon
            # écrire "Au tour de Cortana"

        # écrire un ligne vide afin de créer un espace.
        # si action est égal à 3 et curPlayerID est égal à -1.
            # alors, si tab[0][0] est égal à "_"
                # alors modifier tab[0][0] par "X"
            # sinon
                # modifier tab[0][2] par "X"
        
        # si action est égal à 5 et curPlayerID est égal à -1
            # définir check avec la valeur False
            # pour x allant de 0 à 2.
                # si check n'est pas égal à True
                    # pour y allant de 0 à 2.
                        # si tab[x][y] est égal à "_".
                            # alors définir tempTab avec une copie de tab
                            # modifier tempTab[x][y] par "O"
                            # si une des condition de victoire du joueur est vraie dans tempTab.
                                # modifier tab[x][y] par "X"
                                # modifier check par True
                                # casser la boucle actuelle
            # si check n'est pas True et tab[2][2] égal "_".
                # modifier tab[2][2] par "X"
            # sinon si check n'est pas True
                # modifier tab[2][0] par "X"
        
        # si action égal 7
            # définir check par False
            # pour x allant de 0 à 2
                # si check n'est pas True
                    # pour y allant de 0 à 2
                        # si  tab[x][y] égal "_"
                            # définir tempTab avec une copie de tab
                            # modifier tempTab[x][y] par "X"
                            # si une des conditions de victoire de l'IA est vraie dans tempTab
                                # modifier tab[x][y] par "X"
                                # modifier check par True
                                # casser la boucle actuelle
            # si check n'est pas True
                # modifier check par False
                # pour x allant de 0 à 2
                    # si check n'est pas vrai
                        # pour y allant de 0 à 2
                            # si tab[x][y] égal "_"
                                # modifier tab[x][y] par "X"
                                # modifier check par True
                                # casser la boucle actuelle
        
        # si action égal 9
            # modifier check par False
            # pour x allant de 0 à 2
                # si check n'est pas vrai
                    # pour y allant de 0 à 2
                        # si tab[x][y] égal "_"
                            # modifier tab[x][y] par "X"
                            # modifier check par True
                            # casser la boucle actuelle
        
        # définir cur avec playerSymbole[curPlayerID], le symbole du joueur actuel
        # si une des conditions de victoire du joueur actuel est vraie dans tab
            # afficher le tableau de jeu
            # écrire quel joueur a gagné
            # casser la boucle principale
        # sinon si action égal 9
            # alors écrire "égalité..."
            # casser la boucle principale
        
        # multiplier la valeur de curPlayerID par -1

# exécuter la fonction impossibleMorpion()