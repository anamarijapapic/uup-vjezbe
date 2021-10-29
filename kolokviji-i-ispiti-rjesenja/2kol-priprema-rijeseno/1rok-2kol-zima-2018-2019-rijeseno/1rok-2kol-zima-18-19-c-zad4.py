"""
1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) C

4. Napisati funkciju koja prima niz brojeva i dodatni broj. Funkcija vraca
rjecnik koji ce imati tri kljuca: ’vece’, ’manje’, ’jednako’. Vrijednost svakog
kljuca je lista brojeva koji su veci, manji ili jednaki broju.
"""

def vecemanjejednako(niz, dod):
    rj = {"vece": None, "manje": None, "jednako": None}
    
    #sortiranje u liste
    veci = []
    manji = []
    jednaki = []
    for el in niz:
        if el > dod:
            veci.append(el)
        elif el == dod:
            jednaki.append(el)
        else:
            manji.append(el)
            
    #dodavanje u vrijednosti rjecnika
    rj["vece"] = veci
    rj["manje"] = manji
    rj["jednako"] = jednaki
        
    return rj

lst = [8, 7, 5, 2, 3, 4, 2, 1, 0, 9, 6]
n = 5

print(vecemanjejednako(lst, n))