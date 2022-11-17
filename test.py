def jeuImperatif(lettre):
    reponse = input("devine la lettre connard :")
    n = 1
    while lettre != reponse:
        reponse = input("devine la lettre connard :")
        n = n + 1
    return f"succès! Cela a pris {n} essais grosse merde"

def jeuRecursif(lettre):
    if lettre == input("devine la lettre connard :"):
        return 1
    return jeuRecursif(lettre) + 1