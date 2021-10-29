"""
1. kolokvij zima 2018-2019 C

3. Napisati funkciju koja generira N slucajnih brojeva izmeu 1 i 100 djeljivih
sa 5. Funkcija dobiva N kao parametar.
"""

from random import randint

def generiraj(N):
    brojac = 0
    while brojac < N:
        a = randint(2, 100)
        if a % 5 == 0:
            print(a)
            brojac += 1          

n = int(input("Koliko slucajnih brojeva zelite generirati: "))
generiraj(n)