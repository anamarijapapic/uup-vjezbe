"""
Zadatak 1
Napisati program koji od korisnika čita stringove i sprema ih u listu. 
Kada korisnik upiše samo točku, program završava i ispisuje sve stringove iz liste 
koji su duži od 5 znakova.
"""

lst = []
while True:
    string = input("Unesite string: ")
    if string == ".": #kada se unese samo tocka
        for e in lst:
            if len(e) > 5: #stringovi duzi od 5 znakova
                print(e)
        break
    else:
        lst.append(string)
        print(lst)