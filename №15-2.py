from math import *
proiz = 1
for n in range(1, 11):
    chis = tan(n)
    znam = (n**(0.6*n)) + n + 1
    vur = (chis / znam) * factorial(n)
    proiz *= vur
print(proiz)
