"""
Zadatak 1
Napisati program koji od korisnika cita brojeve. Ako uneseni broj ima
manje od 3 djelitelja, program nastavlja sa citanjem brojeva. U suprotnom
program završava. Program se oslanja na dodatnu funkciju brdjel()
koja prima broj i vraca broj djelitelja primljenog broja. Napisati funkciju
brdjel().
"""

def brdjel(broj):
    brojac = 0
    for i in range (broj, 0, -1):
        if broj % i == 0:
            brojac += 1
    return brojac

while True:
    n = int(input("Unesite broj: "))
    if brdjel(n) >= 3:
        break