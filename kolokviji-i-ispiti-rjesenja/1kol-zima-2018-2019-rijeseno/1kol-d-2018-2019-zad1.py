"""
1. kolokvij zima 2018-2019 D

1. Napisati program koji od korisnika cita brojeve. Program cita brojeve dok
god je upisani broj veci od zbroja svih prethodnih brojeva.
"""

zbroj = 0
upis = 1
while True:
    upis = int(input("Unesite broj: "))
    if zbroj >= upis:
        break
    zbroj += upis
