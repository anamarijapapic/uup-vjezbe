"""
1. kolokvij zima 2018-2019 F

1. Napisati program koji od korisnika cita brojeve. Nakon svakog unesenog
broja program ispisuje razliku prethodno unesenog broja i trenutno unesenog
broja. Za prvi uneseni broj, program ne ispisuje ništa.
"""

prethodni = 0
broj = int(input("Unesite broj: "))
while True:
    prethodni = broj
    broj = int(input("Unesite broj: "))
    print(prethodni - broj)