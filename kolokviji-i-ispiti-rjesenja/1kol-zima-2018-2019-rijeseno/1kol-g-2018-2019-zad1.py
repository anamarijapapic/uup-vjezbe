"""
1. kolokvij zima 2018-2019 G

1. Napisati program koji od korisnika cita dva po dva broja, ukupno 20
brojeva. Svaka dva broja predstavljaju rezultat nekog natjecanja i mogu
biti (1,0), (0,1) ili (0.5, 0.5). Ako uneseni brojevi nisu ispravni, program
ispisuje grešku i traži ponovan unos. Na kraju program ispisuje ukupan
zbroj prvih i ukupan zbroj drugih brojeva.
"""

brojac = 0
zbrojprvih = 0
zbrojdrugih = 0
while brojac < 10:
    prvi = float(input("Prvi broj: "))
    drugi = float(input("Drugi broj: "))
    if (prvi == 1  and drugi == 0) or (prvi == 0 and drugi == 1) or (prvi == drugi == 0.5):
        brojac += 1
        zbrojprvih += prvi
        zbrojdrugih += drugi
    else:
        print("Greska! Molim ponovni unos!")

print("Zbroj prvih brojeva: ", zbrojprvih)
print("Zbroj drugih brojeva: ", zbrojdrugih)
