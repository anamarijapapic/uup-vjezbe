"""
1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) C

3. Napisati funkciju koja prima listu lista. Funkcija vraca listu koja sadrži
duljine svih primljenih lista. Npr. za [ [1,2], [], [2] ], funkcija vraca [2,0,1].
"""

def sveduljine(lst):
    duljina = []
    for e in lst:
        duljina.append(len(e))
    return duljina
            

print(sveduljine([[1,2], [], [2]]))