# Debut

r = 12000
s = 1250
e = 10
rh = 230

# Exo 1

assertionA = (( (365 * 3) / (24 - (16 - 8)) ) * (rh) > r) #True
assertionB = (e * s < r) #False
assertionFinal = assertionA == assertionB #False

# Exo 2

assertionA = ((365 * 3) / (4 - (12 - 8)) * (rh) > r) #False
assertionB = (e * s < r) #False
assertionFinal = assertionA == assertionB  #True

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    return "ne peux pas diviser par zero"

def modulo(x, y):
    return x % y

def salaireNet(brut, coefficient):
    return brut - (brut*coefficient)

def salaireParSeconde(salaireHoraire, heureParJourOuvré, nbJourOuvréParAn):
    # calculer mon salaire annuel
    salaireAnnuel = salaireHoraire * heureParJourOuvré * nbJourOuvréParAn
    # calculer le nombre de seconde dans une année
    nbSecondeParAn = 365 * 24 * 3600
    # je pose et revois la division
    return (nbJourOuvréParAn * heureParJourOuvré * salaireHoraire) / (365 * 24 * 3600)

# definir withdrawFees aui retire un pourcentage à un total en fonction d'un total et d'un pourcentage
def withdrawFees(total, percent):
    # definir fees en fonction d'un total et d'un pourcentage
    fees = total * (percent/100)
    # soustraire fees au total
    result = total - fees
    # retourner la valeur obtenue
    return result

# definir une fonction qui retourne le salaire net en fonction du salaire brut (float) et du secteur d'activité (isPublic > booleen)
def salaireBrutEnNet(salaireBrut, isPublic):
    # si je suis un travailleur du secteur public
    if isPublic:
        # alors je soustrais 15 % de mon salaire brut à mon salaire brut et je l'assigne à la variable salaireNet
        salaireNet = withdrawFees(salaireBrut, 15)
    # sinon je suis un travailleur du secteur privé
    else:
        # alors je soustrais 23 % de mon salaire brut à mon salaire brut et je l'assigne à la variable salaireNet
        salaireNet = withdrawFees(salaireBrut, 23)
    # retourner salaireNet
    return salaireNet

# Fin

# revoie un caractere de type string hasard
# def input(): 

# Exercice :
#     Faire un mini jeu qui affiche un message lorsque input renvoie le bon caractere
#     le caractere doit etre parametrable


# Debut

# defninir une fonction qui prend en argument une lettre sous forme de string
    # definir une variable réponse avec pour valeur une lettre aleatoire donnée par input
    # tant que lettre n'est pas égale à réponse
        # redéfinir la valeur de réponse avec input
    # afficher un message de "succès"

def jeuImperatif(lettre):
    reponse = input()
    n = 0
    while lettre != reponse:
        reponse = input()
        n = n + 1
    return f"succès! Cela a pris {n} essais"

def jeuRecursif(lettre, n=0):
    if lettre == input():
        return n
    return jeuRecursif(lettre, n + 1)

# Fin

def concatWithComma(str1, str2):
    return str(str1) + ", " + str(str2)

# Exo 2
# faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere avec l'ensemble des occurences d'un chiffre eg :
# tableau = [0,1,1,1,0,1,1,0,1]
# la fonction renvoie "0, 4, 7"
# definir la fonction findIndex qui itere sur le tableau, cherchant l'index des differentes occurences de x
def findIndex(tab, x):
    # definir i un index de depart
    i = 0
    # definir chaineRetour comme une chaine de caractere vide
    chaineRetour = ""
    # je defnini un booleen tel que firstTurn est True
    firstTurn = True
    # tant que i est different du nombre d'element dans le tableau
    while i != len(tab):
        # alors j'attribue a une variable la valeur de tableau à l'index i
        selected = tab[i]
        # si selected est egal a x ET que firstTurn est True
        if selected == x and firstTurn:
            # alors on assigne a chaineRetour le retour de str(i)
            chaineRetour = str(i)
            # changer la valeur de firstTurn a False
            firstTurn = False
        # si selected est egal a x
        if selected == x:
            # alors j'assigne le retour de concatWithComma tel que : concatWithComma(chaineRetour, i) a chaineRetour
            chaineRetour = concatWithComma(chaineRetour, i)
        # j'incremente i de 1
        i += 1
    # retourner la chaine retour
    return chaineRetour

    var = input("sdhfhsdf")
    pfc = ["p","f","c"]