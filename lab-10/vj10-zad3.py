"""
Zadatak 3
Napisati funkciju koja prima dvije liste riječi. 
Funkcija vraća listu riječi koje se pojavljuju u obje liste.
"""

def u_obje(lst1, lst2):
    zajednicke = []
    for el in lst1:
        if el in lst2:
            zajednicke.append(el)
    return zajednicke
    

lista1 = ["zbrajanje", "množenje", "oduzimanje", "dijeljenje", "jednako"]
lista2 = ["plus", "puta", "zbrajanje", "minus", "jednako", "oduzimanje"]

print(u_obje(lista1, lista2))