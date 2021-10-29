"""
1. kolokvij zima 2018-2019 I

4. Napisati funkciju koja cita broj po broj dok god korisnik ne unese jedan
broj koji u binarnom prikazu završava sa 1001. Funkcija nakon toga vraca
ta taj broj.
"""

def citaj():
    unos = 0
    while unos & 9 != 9:
        unos = int(input("Unesite broj: "))

citaj()