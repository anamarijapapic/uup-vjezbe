"""
Zadatak 5
Napisati program koji prima brojeve dok se ne upiše 0. Ako je uneseni broj negativan, 
program traži ponovan unos broja dok se ne unese pozitivan broj. Na kraju program 
ispisuje broj pogrešnih (negativnih) unosa.
"""

unos = 1
neg = 0

while unos != 0:
    unos = int(input("Unesite broj: "))
    while unos < 0:
        neg += 1
        unos = int(input("Negativan unos! Unesite broj: "))
        
print("Broj pogrešnih (negativnih) unosa: ", neg)
        
    

        