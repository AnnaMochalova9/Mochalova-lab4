from math import *
summa = 0
for n in range(1, 51):
    numb1 = 1 / (2 * (n**n) + 1)
    numb2 = sin(pi / n)
    vur = numb1 * numb2
    summa = summa + vur
print(summa)
