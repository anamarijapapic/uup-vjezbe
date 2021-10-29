"""
Zadatak 4
Napisati funkciju koja prima string i vraća novi string koji nastaje 
tako da se iz primljenog stringa izbace svi zarezi.
"""

def bez_zareza(string):
    return string.replace(',', "") #zamjena zareza ne-razmakom -> izbacivanje zareza
    
print(bez_zareza("A,n,a,m,a,r,i,j,a"))