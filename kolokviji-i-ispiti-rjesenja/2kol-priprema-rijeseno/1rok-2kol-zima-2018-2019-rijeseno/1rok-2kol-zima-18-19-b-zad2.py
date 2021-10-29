"""
1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) B

2. Napisati funkciju koja prima string i vraca novi string koji nastaje tako
da se iz primljenog stringa izbace svi zarezi.
"""

def bez_zareza(string):
    for c in string:
        return string.replace(",", "")
    
string = "izbac,i,,,sve,z,a,r,e,z,e,"
print(bez_zareza(string))