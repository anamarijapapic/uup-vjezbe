"""
Zadatak 5
Napisati funkciju koja prima dvije liste brojeva i koja računa srednju vrijednost brojeva prve liste, 
a ispisuje brojeve iz druge liste koji su veći od izračunane srednje vrijednosti.
"""

def srednjavrijed(lsta, lstb):
    zbroj = 0
    for e in lsta:
        zbroj += e
    srednjavrijednost = zbroj/len(lsta)
    for e in lstb:
        if e > srednjavrijednost:
            print(e)

lst1 = [8, 9, 60, 23, 40, 12, 21, 40]
lst2 = [8, 9, 55, 23, 86, 12, 60, 40]

srednjavrijed(lst1, lst2)