"""
Zadatak 2
Napisati program koji od korisnika prima dva po dva broja. 
Ako su oba broja pozitivna ispisuje sve brojeve između njih, 
u suprotnom javlja grešku i završava.
"""

x = int(input("Unesite 1. broj: "))
y = int(input("Unesite 2. broj: "))

if x > 0 and y > 0:
    if x < y:
        for i in range (x+1, y):
            print(i)
            i += 1
    if x > y:
        for i in range (x-1, y, -1): #treća stavka u for zagradi je step (pa ispada silazno)
            print(i)
else:
    print("Greška!")