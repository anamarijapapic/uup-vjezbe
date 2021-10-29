"""
1. kolokvij zima 2018-2019 E

2. Napisati program koji od korisnika cita 10 pozitivnih brojeva. Nakon
svakog unosa, program ispisuje sve djelitelje unesenog broja. Program
ignorira negativne brojeve. Ako korisnik unese 0, program ispisuje "kraj"
i prekida se.
"""

brojac = 0
while brojac < 10:
    unos = int(input("Unesite broj: "))
    if unos == 0:
        print("Kraj.")
        break
    elif unos < 0:
        continue
    else:
        brojac += 1
        for i in range (1, unos + 1):
            if unos % i == 0:
                print(i)

