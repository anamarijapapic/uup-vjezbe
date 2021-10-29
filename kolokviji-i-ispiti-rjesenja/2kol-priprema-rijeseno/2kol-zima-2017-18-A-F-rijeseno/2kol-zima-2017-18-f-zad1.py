"""
2. Kolokvij Zima 2017-18 F

1. Napisati funkciju koja prima listu brojeva. Funkcija vraca listu brojeva iz
primljene liste koji su nisu djeljivi sa nijednim drugim brojem iz primljene
liste. Npr. za listu [ 6, 2, 7, 9 ], funkcija vraca listu [2,7,9].
"""

def nedjeljivi(lst):
    nova = []
    for i in lst: #secemo jedan po jedan el. liste
        cnt = 0 #brojac na nula
        for j in lst: #takoder secemo jedan po jedan el. liste
            if i % j == 0: #ako je ostatak 0 znaci da su djeljivi, pa dizemo brojac
                cnt += 1
        if cnt == 1: #onaj koji je djeljiv s "drugima" samo 1 put ide u listu jer je onda nedjeljiv,
        #znaci da mu je brojac osta na 1 jer se podilia sam sa sobom i to je to
            nova.append(i)
    return nova

print(nedjeljivi([6, 2, 7, 9]))