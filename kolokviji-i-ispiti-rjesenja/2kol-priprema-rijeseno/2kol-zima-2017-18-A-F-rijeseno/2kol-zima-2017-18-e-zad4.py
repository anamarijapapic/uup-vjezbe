"""
2. Kolokvij Zima 2017-18 E

4. Napisati funkciju koja prima listu lista brojeva. Funkcija od brojeva u
listi konstruira rjecnik koji kao kljuceve ima najveci broj iz svake pojedine
liste, a svakom kljucu je kao vrijednost pridružena ta lista.
"""

def konstruiraj(lst):
    rj = {}
    for i in lst:
        najv = i[0]
        for e in i:
            if e > najv:
                najv = e
        k = najv
        rj[k] = i
    return rj
    
print(konstruiraj([[5, 8, 10, 25, 2], [80, 90, 40, 3], [77, 11, 42]]))