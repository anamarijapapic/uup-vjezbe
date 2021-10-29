"""
2. Kolokvij Ljeto 2016-17

1. Napisati funkciju koja prima listu brojeva. Funkcija vraca listu koja sadrži
svaki broj samo jednom. Npr. za listu [6,5,6,4,8,4], funkcija vraca [6,5,4,8].
"""

def samojednom(lst):
    nova = []
    for e in lst:
        if e not in nova:
            nova.append(e)
    return nova
             
print(samojednom([6,5,6,4,8,4]))  