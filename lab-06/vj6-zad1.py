"""
Zadatak 1
Napisati program koji prima broj od korisnika i provjerava njegove bitove. 
Za svaki bit postavljen na 1 program pita korisnika da unese broj. 
Program na kraju ispisuje zbroj unesenih brojeva.
"""

broj = int(input("Unesite broj: "))
print(bin(broj))

zbroj = 0

for i in range (broj):
    if broj & 1: #ako je True i ulazi u if petlju znaci da je ta znamenka broja u bin. sustavu 1
        unos = int (input("Unesite broj: "))
        zbroj += unos
    broj = broj >> 1 #shiftamo broj u desno kako bismo dalje ispitivali

print("Zbroj brojeva je:", zbroj)
