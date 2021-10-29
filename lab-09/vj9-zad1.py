"""
Zadatak 1
Napisati funkciju koja prima listu brojeva i ispisuje samo parne elemente. 
Napisati drugu funkciju koja prima listu brojeva i ispisuje samo elemente na parnim indeksima.
"""

def parniel(lst):
    for e in lst:
        if e % 2 == 0:
            print(e)
            
def parniindeks(lst):
    for i in range(len(lst)):
        if i % 2 == 0:
            print(lst[i])

lst1 = [8, 9, 55, 23, 86, 12, 7, 40]

parniel(lst1)
print()
parniindeks(lst1)