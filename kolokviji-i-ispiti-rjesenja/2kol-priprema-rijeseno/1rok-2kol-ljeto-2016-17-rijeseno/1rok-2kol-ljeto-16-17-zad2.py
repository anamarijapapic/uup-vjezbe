"""
1. Rok 2. Kolokvij Ljeto 2016-17

2. Napisati funkciju koja prima dva stringa sastavljena od cijelih pozitivnih
brojeva odvojenih zarezom. Oba stringa sadrže isti broj brojeva. Funkcija
vraca string (istog formata) gdje su elementi zbroj dva broja iz prvog i
drugog stringa. Npr. za „3,14,2,10“ i „6,11,5,5“, funkcija vraca „9,25,7,15“.
"""

def zbroji(string1, string2):
    lst1 = string1.split(",")
    lst2 = string2.split(",")
    rez = []
    for e1, e2 in zip(lst1, lst2):
        zbr = int(e1) + int(e2)
        rez.append(str(zbr))
    return ",".join(rez)
    
print(zbroji("3,14,2,10", "6,11,5,5"))