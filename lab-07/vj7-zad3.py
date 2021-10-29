"""
Zadatak 3
Napisati funkciju koja prima cijeli broj i vraća koliko taj broj ima djelitelja. 
Npr. za 15, funkcija vraća 4 (za 1, 3, 5 i 15). Napisati pomoćnu funkciju djelitelj 
koja provjerava je li broj djelitelj drugog broja (funkcija vraća boolean).
"""

def djelitelj(x,y):
    if x % y == 0:
        return True
    else:
        return False

def br_djelitelja(n):
    brojac = 0
    for i in range (1, n+1):
        if n % i == 0:
            brojac += 1
            print(i, djelitelj(n, i)) #provjera! (šaljemo u pom. funkciju)
    return brojac


broj = int(input("Unesite broj: "))

print(br_djelitelja(broj))