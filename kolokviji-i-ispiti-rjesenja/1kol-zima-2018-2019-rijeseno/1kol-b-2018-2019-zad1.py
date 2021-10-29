"""
1. kolokvij zima 2018-2019 B

1. Napisati program koji od korisnika cita brojeve. Program cita brojeve dok
god je upisani broj veci od svih prethodnih brojeva.
"""

prethodni = 0
unos = 1
while unos > prethodni:
    unos = int(input("Unesite broj: "))
    if unos > prethodni:
        prethodni = unos
    unos = int(input("Unesite broj: "))