"""
1. kolokvij zima 2018-2019 H

1. Napisati program koji od korisnika cita brojeve. Nakon svakog unesenog
broja program ispisuje razliku prethodno unesenog broja i trenutno unesenog
broja. Za prvi uneseni broj, program ne ispisuje ništa.
"""

a = int(input("Unesite broj: "))
prethodni = a
while True:
    a = int(input("Unesite broj: "))
    print(prethodni - a)
    prethodni = a
