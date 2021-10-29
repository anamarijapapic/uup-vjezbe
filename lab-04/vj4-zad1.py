"""
Zadatak 1
Napišite program koji za unesene duljine kateta računa hipotenuzu pravokutnog trokuta. 
Napomena: korijen se računa uz pomoć funkcije math.sqrt() koja se nalazi u biblioteci math 
(na početku programa potrebno je uključiti biblioteku naredbom import).
"""

import math

a = int(input("Unesite 1. katetu pravokutnog trokuta: "))
b = int(input("Unesite 2. katetu pravokutnog trokuta: "))

if a <= 0 or b <= 0:
    print("Krivi unos")
else:
    c = math.sqrt(a**2 + b**2)
    print("Duljina hipotenuze pravokutnog trokuta je: ", c)