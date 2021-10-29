"""
Zadatak 4
Napisati funkciju koja za dobiveni broj i mjesto vraća znamenku na zadanom mjestu. 
Npr. za broj _45678_ i mjesto 4 ispisuje znamenku _5_. Mjesto se broji od najmanje značajne znamenke.
"""

broj = int(input("Unesite broj: "))
mjesto = int(input("Unesite mjesto (brojeci od LSB-a): "))

def znamenka(a, b):
    for i in range(b - 1):
        a = a // 10     #kida znamenke s desna do one koja nam je potrebna
    return a % 10       #znamenku koja nam treba konacno dobivamo kao ostatak dijeljenja s 10

print(znamenka(broj, mjesto))