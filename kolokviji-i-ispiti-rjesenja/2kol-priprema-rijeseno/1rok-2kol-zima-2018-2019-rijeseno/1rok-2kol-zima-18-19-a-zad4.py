"""
1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) A

4. Napisati funkciju koja prima rjecnik i broj B. Vrijednosti u rjecniku su
liste brojeva. Funkcija vraca True ako su svi brojevi u svim listama u
rjecniku manji od B.
"""
def manjiodB(rjecnik, B):
    for k in rjecnik:
        for v in rjecnik[k]:
            if v >= B:
                return False #cim nade jedan da je veci od B -> vraca False
    return True #inace True

B = ord('B') #vrijednost od B -> 66

rjecnik = {1: [1, 2, 3, 4, 5], 2: [10, 20, 30, 40, 50], 3: [44, 48, 52, 56, 60, 64]}
rjecnik1 = {1: [1, 2, 3, 4, 5], 2: [10, 20, 30, 40, 50, 100], 3: [44, 48, 52, 56, 60, 64]}

print(manjiodB(rjecnik, B))
print(manjiodB(rjecnik1, B))