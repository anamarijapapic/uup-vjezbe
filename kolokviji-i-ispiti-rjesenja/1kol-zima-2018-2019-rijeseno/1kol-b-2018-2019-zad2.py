"""
1. kolokvij zima 2018-2019 B

2. Napisati program koji korisnika cita brojeve. Program cita brojeve dok
god su upisani brojevi naizmjenice parni i neparni.
"""

unos = int(input("Unesite broj: "))
prethodni = unos
while True:
    unos = int(input("Unesite broj: "))
    if (unos % 2 == 0 and prethodni % 2 == 0) or (unos % 2 == 1 and prethodni % 2 == 1):
        break
    prethodni = unos
