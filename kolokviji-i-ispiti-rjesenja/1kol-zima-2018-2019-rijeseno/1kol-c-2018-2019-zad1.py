"""
1. kolokvij zima 2018-2019 C

1. Napisati program koji od korisnika cita dva po dva broja, ukupno 20
brojeva. Svaka dva broja predstavljaju rezultat nekog natjecanja i oba
broja moraju biti pozitivna, a zbroj im mora biti 100. Ako uneseni brojevi
nisu ispravni, program ispisuje grešku i traži ponovan unos. Na kraju
program ispisuje prosjek prvih i prosjek drugih brojeva.
"""

zbroj_a, zbroj_b = 0, 0
for i in range(10):
    a = int(input("Unesite prvi broj: "))
    b = int(input("Unesite drugi broj: "))
    if a <= 0 or b <= 0 or (a + b) != 100:
        print("Greska! Molim ponovan unos!")
        a = int(input("Ponovno unesite prvi broj: "))
        b = int(input("Ponovno unesite drugi broj: "))
    zbroj_a += a
    zbroj_b += b    

print("Prosjek prvih brojeva je: ", zbroj_a/10)
print("Prosjek drugih brojeva je: ", zbroj_b/10)