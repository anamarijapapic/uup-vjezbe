"""
1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) B

4. Napisati funkciju koja prima rjecnik koji kao kljuceve ima brojeve, a kao
vrijednosti liste brojeva. Funkcija vraca True ako je svaki kljuc jednak
prosjeku brojeva u pridruženoj listi.
"""

def jednakprosjeku(rj):
    for k in rj:
        zbr = 0
        for e in rj[k]: #value je lista pa secemo ovako po elementima
            zbr += e
        if k != zbr / len(rj[k]):
            return False
    return True
    
           

rjecnik = {20: [10, 30, 0, 40], 5: [1, 4, 8, 7], 50: [10, 60, 40, 90, 50]}
rjecnik2 = {8: [55, 4], 16: [7, 64, 1,]}

print(jednakprosjeku(rjecnik))
print(jednakprosjeku(rjecnik2))