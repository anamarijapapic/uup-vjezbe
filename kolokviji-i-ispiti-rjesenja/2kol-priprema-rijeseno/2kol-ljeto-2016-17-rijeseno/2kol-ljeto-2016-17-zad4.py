"""
2. Kolokvij Ljeto 2016-17

4. Napisati funkciju koja prima listu lista brojeva. Funkcija od brojeva u
listi konstruira rjecnik koji kao kljuceve ima zbroj svake pojedine liste, a
svakom kljucu je kao vrijednost pridružena ta lista.
"""

def konstruiraj(lst):
    rj = {}
    for i in lst:
        zbr = 0
        for e in i:
            zbr += e
        k = zbr #kljuc
        rj[k] = i #vrijednost
    return rj
    
print(konstruiraj([[5, 8, 10, 25, 2], [80, 90, 40, 3], [77, 11, 42]]))