"""
1. kolokvij zima 2018-2019 G

3. Napisati funkciju koja generira N slucajnih brojeva izmeu 1 i 100 djeljivih
sa 5. Funkcija dobiva N kao parametar.
"""

from random import randint

def generiraj(N):
    brojac = 0
    while brojac < N:
        n = randint(2, 100)
        if n % 5 == 0:
            brojac += 1
            print(n)

koliko = int(input("Koliko slucajnih brojeva zelite generirati: "))
generiraj(koliko)