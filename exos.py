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
    return x / y

def modulo(x, y):
    return x % y

def salaireNet(brut, coefficient):
    return brut - (brut*coefficient)

def salaireParSeconde(salaireHoraire, heureParJourOuvré, nbJourOuvréParAn):
    return nbJourOuvréParAn * heureParJourOuvré * (salaireHoraire / 3600)

# Fin