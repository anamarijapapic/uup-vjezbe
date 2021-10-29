"""
Zadatak 5
Napisati funkciju koja prima rječnik gdje su ključevi imena kandidata, 
a vrijednost broj glasova koje je dobio na izborima. 
Funkcija vraća novi rječnik koji sadrži imena kandidata i postotak dobivenih glasova.
"""

def funkcija(rjecnik):
    novirjecnik = {}
    glasovi = 0
    for e in rjecnik:
        glasovi += rjecnik[e]
    for e in rjecnik:
        novirjecnik[e] = str(int((rjecnik[e] / glasovi) * 100)) + "%" #izracun postotka
    return novirjecnik

izbori = {"Milanovic" : 30, "Plenkovic" : 40, "Kolinda" : 45, "Kerum" : 20 }
print(funkcija(izbori))