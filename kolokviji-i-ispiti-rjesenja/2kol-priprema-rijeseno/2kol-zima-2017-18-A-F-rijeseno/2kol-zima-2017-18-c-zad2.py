"""
2. Kolokvij Zima 2017-18 C

2. Napisati program koji od korisnika cita slova. Ako korisnik ne upiše slovo
program ponavlja unos. Ako korisnik upiše tocku, program završava i
ispisuje broj upisanih suglasnika i samoglasnika.
"""

samogl = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

brsamogl = 0
brsugl = 0

while True:
    unos = input("Unesite slovo: ")
    if unos.isalpha() and unos in samogl:
        brsamogl += 1
    elif unos.isalpha() and unos not in samogl:
        brsugl += 1
    elif unos == ".":
        break
    else:
        print("Ponovite unos!")
        
print("Broj samoglasnika: ", brsamogl, "\nBroj suglasnika: ", brsugl)