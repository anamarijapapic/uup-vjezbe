"""
1. kolokvij zima 2018-2019 D

3. Napisati funkciju koja cita dva po dva broja dok god korisnik ne upiše oba
pozitivna broja. Funkcija nakon toga vraca ta dva broja.
"""

def obapoz():
    x = 0
    y = 0
    while x <= 0 or y <= 0:
        x = int(input("Prvi broj: "))
        y = int(input("Drugi broj: "))
        if x > 0 and y > 0:
            return x, y
        
print(obapoz())
    