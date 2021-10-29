"""
6.	Napisati rekurzivnu funkciju koja vraća zbroj svih brojeva između dva broja koja dobije kao parametre.
"""

def rekzbrojizmedu(a, b):
    if a == b:
        return 0
    elif a < b:
        return a + rekzbrojizmedu(a+1, b)
    else:
        return b + rekzbrojizmedu(b+1, a)
    
print(rekzbrojizmedu(2, 8)) # 2 + 3 + 4 + 5 + 6 + 7
print(rekzbrojizmedu(1, 9)) # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8