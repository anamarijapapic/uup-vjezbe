"""
5.	Napisati funkciju veca2() koja vraća veću vrijednost između dvije. 
Napisati funkciju veca5() koja vraća najveću vrijednost od 5 vrijednosti i 
koja se oslanja na funkciju veca2() te ne koristi odluke.
"""

def veca2(a, b):
    if a >= b:
        return a
    else:
        return b
    
def veca5(a, b, c, d, e):
    return veca2(veca2(veca2(a, b), veca2(c, d)), e)
    
print(veca5(2, 18, 15, 32, -6))
print(veca5(98, 5647, 571, -632, 8795))