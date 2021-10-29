"""
2. Kolokvij Zima 2017-18 B

3. Napisati program koji od korisnika cita stringove i sprema ih u listu. Kada
korisnik upiše samo tocku, program završava i ispisuje sve stringove iz listi
koji su duži od 5 znakova.
"""

lst = []
while True:
    unos = input("Unesite string: ")
    if unos == ".":
        break
    lst.append(unos)
for e in lst:
    if len(e) > 5:
        print(e)