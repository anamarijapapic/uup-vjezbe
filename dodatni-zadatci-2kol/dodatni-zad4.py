"""
4.	Napisati funkciju koja prima niz brojeva i dodatni broj. Funkcija vraća rječnik 
koji će imati tri kljuca: ’vece’, ’manje’, ’jednako’. Vrijednost svakog kljuca je 
lista brojeva koji su veći, manji ili jednaki broju.
"""

def vecemanjejednako(niz, dod):
    rj = {"vece": None, "manje": None, "jednako": None}
    veci = []
    manji = []
    jednaki = []
    
    for i in niz:
        if i > dod:
            veci.append(i)
        elif i == dod:
            jednaki.append(i)
        elif i < dod:
            manji.append(i)
    
    rj["vece"] = veci
    rj["manje"] = manji
    rj["jednako"] = jednaki
    
    return rj
            
print(vecemanjejednako([0, 1, 3, 5, 7, 9, 8, 6, 4, 2], 5))