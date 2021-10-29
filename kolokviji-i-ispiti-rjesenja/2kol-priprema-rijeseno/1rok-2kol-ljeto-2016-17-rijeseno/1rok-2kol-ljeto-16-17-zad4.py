"""
1. Rok 2. Kolokvij Ljeto 2016-17

4. Napisati funkciju koja prima rjecnik i jedan broj. Vrijednosti u rjecniku
su liste brojeva. Funkcija dodaj taj broj svim listama u rjecniku.
"""

def dodaj(rj, br):
    for k in rj:
        rj[k].append(br)
    return rj

rjecnik = {1: [2, 3, 4], 2: [2, 4, 6, 8], 3: [1, 3, 5, 7, 9]}

print(dodaj(rjecnik, 5))