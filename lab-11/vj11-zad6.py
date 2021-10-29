"""
Zadatak 6
Napisati funkciju koja prima dvije liste riječi. Funkcija vraća rječnik koji sadrži riječi 
iz prve liste kao ključeve i boolean vrijednosti koja označava da li se riječ pojavljuje u drugoj listi.
"""

def liste(lst1, lst2):
    rjecnik = {}
    for e in lst1:
        if e in lst2:
            rjecnik[e] = True #rijec u obe liste
        else:
            rjecnik[e] = False #rijec nije u obe liste
    return rjecnik

prva = ["zmija", "pas", "macka", "labud", "zec", "crv", "pauk"]
druga = ["ptica", "jelen", "zmija", "macka", "pauk", "riba",]

print(liste(prva, druga))