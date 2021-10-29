"""
2. Kolokvij Zima 2017-18 D

2. Napisati funkciju koja prima string i vraca novi string koji nastaje tako
da se iz primljenog stringa izbace svi zarezi.
"""

def bezzareza(string):
    return string.replace(",", "")

print(bezzareza(",i,z,b,a,c,i,,,, S,V,,,E,, zare,ze!,"))