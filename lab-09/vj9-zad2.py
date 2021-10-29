"""
Zadatak 2
Napisati funkciju koja prima listu brojeva i vraća boolean. 
Funkcija vraća True samo ako su sve vrijednosti u listi poredane po veličini (rastući niz).
"""

def rastuci(lst):
    prethodni = lst[0]
    for e in lst[1:]:
        if e <= prethodni:
            return False
        prethodni = e
    return True   

"""
# 2. nacin
def rastuci2(lst):
    prethodni = lst[0]
    for i in range(1, len(lst)):
        if lst[i] <= prethodni:
            return False
        prethodni = lst[i]
    return True
""" 

lst1 = [8, 9, 55, 23, 86, 12, 7, 40]
lst2 = [12, 23, 30, 41, 55, 68]

print(rastuci(lst1))
print(rastuci(lst2))