"""
2. Kolokvij Zima 2017-18 C

4. Napisati funkciju koja prima rjecnik sa stringovima kao kljucevima i listama
brojeva kao vrijednostima. Za svaki kljuc u rjecniku, funkcija racuna
najveci broj iz pridružene liste. Funkcija vraca rjecnik sastavljen od istih
kljuceva i pridruženih najvecih brojeva.
"""

def najveciulst(rj):   
    for k in rj: #sece kljuc po kljuc
        najv = rj[k][0] #za svaki kljuc prvu vrijednost u listi namista kao najvecu
        for e in rj[k]:
            if e > najv: #sece po listi, ako je neki el. veci on postaje najveci
                najv = e
        rj[k] = najv #na kraju svakom kljucu pridruzimo vrijednost njegovog najveceg broja iz liste
    return rj #vracamo promijenjen rjecnik

rjecnik = {"haha": [10, 30, 0, 40], "hehe": [1, 4, 8, 7], "hihi": [10, 60, 40, 90, 50]}

print(najveciulst(rjecnik))