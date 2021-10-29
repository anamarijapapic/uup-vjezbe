"""
Zadatak 2
Napisati funkciju koja ispisuje sve proste faktore nekog broja. 
Napisati pomoćnu funkciju koja provjerava je li broj prost.
"""

def ispis_prostfaktor(n):
    #odabire se prvi najmanji prosti faktor (a to je 2)
    p = 2
    brojac = 0
    while n > 1:
        #provjerava se je li broj djeljiv s tim faktorom
        #ako je --> faktor ispisujemo i novi broj dobijemo dijeljenjem s posljednjim faktorom
        if n % p == 0:
            print(p)
            brojac += 1
            n = n / p
        #ako faktor nije sadržan u broju --> odabiremo za jedan veci faktor
        else:
            p = p + 1
    return brojac

def prost(n): #primit ce argument brojac iz funkcije ispis_prostfaktor kao n
    if n == 1:
    #ako je brojac onda ostao na 1 --> prost
        return True
    else:
        #brojac je povecao iznos --> vise faktora --> nije prost
        return False
            
broj = int(input("Unesite broj: "));

#obavit ce funkciju ispis_prostfaktor (ispisivanje) "unutar" funkcije prost
if prost(ispis_prostfaktor(broj)):
    print("Uneseni broj je prost.")
else:
    print("Uneseni broj nije prost.")