"""
Zadatak 3
Napisati funkciju koja za tri broja dobivena preko parametara vraća srednji broj među njima. 
Na primjer za 64, 57 i 88 vraća broj 64.
"""

def srednji(a, b, c):
    if (a > b and a < c) or (a < b and a > c):
        return a
    elif (b > a and b < c) or (b < a and b > c):
        return b
    elif (c > a and c < b) or (c < a and c > b):
        return c
    else:
        print("Neki od brojeva su jednaki.")

print("Unesite tri broja: ")
a = int(input())
b = int(input())
c = int(input())

print("Srednji broj je: ", srednji(a, b, c))