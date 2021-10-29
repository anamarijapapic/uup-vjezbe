"""
Zadatak 1
Napisati funkciju koja generira cijeli broj u rasponu od 1 do 100. 
Funkcija generira parni ili neparni broj ovisno o dobivenom parametru p = 'par' ili 'nepar'. 
Funkcija se oslanja na funkciju random.randint().
"""

from random import randint

def generiraj(p):
    n = randint(1, 100)
    if p == "par":
        if n % 2 == 0:
            return n
        else:
            return n + 1
    elif p == "nepar":
        if n % 2 != 0:
            return n
        else:
            return n + 1
    else:
        return ("Greska! Krivi unos!")
    
parnepar = input("Parni ili neparni broj? (par/nepar): ")
print(generiraj(parnepar))




