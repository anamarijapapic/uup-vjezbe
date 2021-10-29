"""
Zadatak 4
Napisati program koji od korisnika prima 10 brojeva. Na kraju program ispisuje 
koliko je brojeva bilo parno i koliko neparno. Program ignorira unesene nule.
"""

par = 0
nepar = 0

for i in range (1, 11):
    unos = int(input("Unesite broj: "))
    if unos == 0:
        continue
    elif unos % 2 == 0:
        par += 1
    else:
        nepar += 1
        
print("Parnih brojeva: ", par)
print("Neparnih brojeva: ", nepar)
    
    

