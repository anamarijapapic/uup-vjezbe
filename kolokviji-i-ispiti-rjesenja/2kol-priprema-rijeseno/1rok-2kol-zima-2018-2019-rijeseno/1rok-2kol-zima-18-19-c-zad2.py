"""
1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) C

2. Napisati funkciju koja prima jedan string. String je u obliku „(A+B)**N“,
gdje su A, B i N cijeli pozitivni brojevi. Funkcija vraca rezultat tog izraza.
"""

def izracun(string):
    prvidio, n = string.split("**") #(A+B)  N
    aplusb = prvidio[1:4] #1+4
    a, b = aplusb.split("+") #1  4
    n = int(n)
    a = int(a)
    b = int(b)
    return (a + b) ** n
    
izraz = "(1+4)**2"
print(izracun(izraz))