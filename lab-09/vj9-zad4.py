"""
Zadatak 4
Napisati funkciju koja prima dvije liste brojeva i koja ispisuje brojeve iz prve liste 
koji su djeljivi sa 3, a ujedno se nalaze i u drugoj listi.
"""

def djeljivipresjek(lsta, lstb):
    for e in lsta:
        if e % 3 == 0 and e in lstb:
            print(e)
                    
lst1 = [8, 9, 60, 23, 40, 12, 21, 40]
lst2 = [8, 9, 55, 23, 86, 12, 60, 40]
    
djeljivipresjek(lst1, lst2)