"""
Zadatak 1
Napiši funkciju koja će za dva ulazna parametra riječ i znak, ispisati sve riječi (stringove) koji se mogu
dobiti postavljanjem unesenog znaka na bilo koje mjesto u unesenoj riječi (stringu). Korisnik unosi riječ
i znak. Funkcija nema povratne vrijednosti.
"""

def funkcija(rijec, znak):
    for e in range(len(rijec) + 1):
       print(rijec[:e] + znak + rijec[e:])
funkcija("ZNAK", "T")