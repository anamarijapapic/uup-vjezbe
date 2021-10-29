"""
1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) C

1. Napisati funkciju koja prima dvije liste brojeva iste dužine. Funkcija
vraca isprepletene liste. Npr. za liste [1,3,5] i [2,4,6], funkcija vraca listu
[1,2,3,4,5,6].
"""

def isprepleti(lst1, lst2):
    lst = []
    for i in range(len(lst1)):
        #clan prve pa clan druge dodajemo u novu listu, za svaki indeks
        lst.append(lst1[i])
        lst.append(lst2[i])
    return lst

lsta = [1, 3, 5]
lstb = [2, 4, 6]

print(isprepleti(lsta, lstb))