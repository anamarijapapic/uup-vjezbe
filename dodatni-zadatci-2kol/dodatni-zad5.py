"""
5.	Napisati funkciju koja prima rječnik sa stringovima kao ključevima i listama brojeva 
kao vrijednostima. Za svaki ključ u rječniku, funkcija računa najveći broj iz pridružene liste. 
Funkcija vrača rječnik sastavljen od istih ključeva i pridruženih najvećih brojeva.
"""

def najveci(rj):
    for k in rj:
        naj = rj[k][0] #prvi clan svake liste uzimamo kao najveci
        for e in rj[k]: #secemo po listi
            if e > naj: #ako je neki clan veci, on postaje najveci
                naj = e
            rj[k] = naj #svakom kljucu pridruzujemo najveceg kao vrijednost
    return rj

rjecnik = {"prvi": [19, 17, 33, 22], "drugi": [47, 88, 11], "treci": [99, 20]}
print(najveci(rjecnik))