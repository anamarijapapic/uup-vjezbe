"""
Zadatak 7
Napisati program koji telefonski broj tipa 0800-CALL-ME pretvara u telefonski broj sastavljen 
samo od znamenki i povlaka. Pretvaranje se vrši uz pomoć rječnika koji za svako slovo definira 
odgovarajuću znamenku (slovima 'a', 'b' i 'c' odgovara znamenka 1, ...).
"""

telefon = "0800-CALL-ME"
broj = ""

rjecnik = {"a": 1, "b": 1, "c": 1, 
           "d": 2, "e": 2, "f": 2, 
           "g": 3, "h": 3, "i": 3, 
           "j": 4, "k": 4, "l": 4, 
           "m": 5, "n": 5, "o": 5, 
           "p": 6, "q": 6, "r": 6, 
           "s": 7, "t": 7, "u": 7, 
           "v": 8, "w": 8, "x":8, 
           "y": 9, "z": 9}

for e in telefon:
    if e.isalpha():
        slovo = e.lower()
        broj += str(rjecnik[slovo])
    else:
        broj += str(e)
        
print(broj)