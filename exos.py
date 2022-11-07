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

# Fin