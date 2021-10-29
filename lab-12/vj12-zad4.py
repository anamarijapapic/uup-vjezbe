"""
Zadatak 4
Napisati igru vješalo koristeći se rječnikom koji sadrži nazive filmova. Također, funkciju koja slučajno
odabire film iz navedenog rječnika. Korisnik unosi znakove a dozvoljen broj pokušaja je duljina riječi
koju pogađa.
"""

from random import randint

naslovi = {1: "Trainspotting", 2: "Dogtooth", 3: "Clockwork Orange", 4: "The Lobster", 5: "Pulp Fiction",
           6: "The Usual Suspects", 7: "Dallas Buyers Club", 8: "Once Upon a Time in Hollywood", 
           9: "The Girl with the Dragon Tattoo", 10: "Three Billboards Outside Ebbing, Missouri"}

def slucajni_odabir():
    k = randint(1, len(naslovi))
    return naslovi[k]

def iscrtkaj_mjesta(naslov):
    rjesenje = []
    for char in naslov:
        if char == " ":
            rjesenje.append(" ")
        elif char == ",":
            rjesenje.append(",")
        else:
            rjesenje.append("-")
    return rjesenje

def popuni(rjesenje, slovo, naslov):
    for i, char in enumerate(naslov):
        if slovo == char.lower():
            rjesenje[i] = char
    return slovo in naslov.lower()

film = slucajni_odabir()
brojac = len(film)
rjesenje = iscrtkaj_mjesta(film)

while True:
    print("Pogodite naziv filma: ","".join(rjesenje))
    print("Broj pokusaja:", brojac, "/", len(film))
    slovo = input("Unesite slovo: ")
    brojac -= 1
    popuni(rjesenje, slovo, film)
    
    if brojac == 0: #poraz
        print()
        print("Izgubili ste, nemate vise dostupnih pokusaja.")
        print("Rjesenje: ", film)
        break
    
    if "".join(rjesenje) == film: #pobjeda
        print()
        print("Rjesenje: ", "".join(rjesenje))
        print("Bravo! Rijeseno!")
        break