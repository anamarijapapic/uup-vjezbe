"""
Zadatak 2
Napisati funkciju koja prima listu parova i vraća dvije liste. 
Prva lista sadrži samo prve elemente parova, a druga lista druge elemente parova.
"""

def parovi(lst):
    prvi = []
    drugi = []
    for i, j in lst:
        prvi.append(i)
        drugi.append(j)
    return prvi, drugi

lista = [(1, 4), (8, 6), (2, 0), (5, -3), (7, 11)]

print(parovi(lista))