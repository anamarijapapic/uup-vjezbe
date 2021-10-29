"""
1. Rok 2. Kolokvij Ljeto 2016-17

1. Napisati funkciju koja prima listu brojeva. Funkcija vraca listu koja sadrži
boolean vrijednosti. Vrijednost u listi je True samo ako je taj broj djeljiv
sa iducim brojem. Npr. za listu [6,3,1,4,2,4], funkcija vraca [T,T,F,T,F,F].
"""

def vratibool(lst):
    b = []
    for i in range(len(lst) - 1):
        if lst[i] % lst[i + 1] == 0:
            b.append(True)
        else:
            b.append(False)
    b.append(False) #za zadnji el. u listi uvik dodat jos jedan False, jer nema sljedbenika
    return b

print(vratibool([6, 3, 1, 4, 2, 4]))