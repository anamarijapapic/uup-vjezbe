"""
Zadatak 3
IP adresa je sastavljena od četiri dijela (npr. 196.68.33.1) gdje je svaki dio 
kodiran na 8 bitova, tako da je IP adresa zapravo 32-bitni broj. 
Adresa iz prethodnog primjera kodira se brojem 3292799233. Treba napisati izraz 
(ili izraze) koji za uneseni cijeli broj između 0 i 2147483647 provjerava:
a) jesu li prva dva dijela adrese 196 i 68
b) jesu li zadnja dva dijela adrese manji od 128
c) jesu li prvi i zadnji dio adrese jednaki.
"""

adresa = int(input("Unesite broj: "))

#a
if adresa >> 24 == 196 and (adresa >> 16) & 68 == 68:
    print(True)
else:
    print(False)
    
#b
if (adresa & 128) < 128 and ((adresa >> 8) & 128) < 128:
    print(True)
else:
    print(False)
    
#c
if adresa >> 24 == adresa & (adresa >> 24):
    print(True)
else:
    print(False)