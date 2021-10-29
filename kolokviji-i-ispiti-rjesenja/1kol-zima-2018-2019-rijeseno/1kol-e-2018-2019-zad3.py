"""
1. kolokvij zima 2018-2019 E

3. Napisati funkciju koja cita dva po dva broja dok god korisnik ne unese
dva broja koja su oba veca od prethodna dva broja. Funkcija nakon toga
vraca ta dva broja. Prva dva unesena broja se ne vracaju.
"""

def dvapodva():
    prvi = int(input("Unesite prvi broj: "))
    drugi = int(input("Unesite drugi broj: "))
    prethprvi = prvi
    prethdrugi = drugi
    while True:
        prvi = int(input("Unesite prvi broj: "))
        drugi = int(input("Unesite drugi broj: "))
        if prvi > prethprvi and drugi > prethdrugi:
            return prvi, drugi
        prethprvi = prvi
        prethdrugi = drugi

print(dvapodva())