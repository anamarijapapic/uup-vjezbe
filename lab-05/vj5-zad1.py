"""
Zadatak 1
Napisati program koji generira slučajne brojeve između 0 i 1000. 
Program ispisuje samo brojeve koji su veći od 100, a manji od 500. 
Program završava kada ispiše 10 brojeva.
"""

from random import randint

ispis = 0
while ispis != 10:
    x = randint(0, 1000)
    if x > 100 and x < 500:
        print(x)
        ispis += 1

