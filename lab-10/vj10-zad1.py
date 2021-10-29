"""
Zadatak 1
Napisati funkciju koja prima listu brojeva i listu stringova. 
Funkcija ispisuje samo stringove na indeksima zadanim u listi brojeva.
"""

def brstr(brojevi, stringovi):
    for i in brojevi:
        print(stringovi[i])      

num = [6, 2, 4, 1, 0, 5]
zivotinje = ["pas", "macka", "ptica", "riba", "hrcak", "konj", "zmija"]

brstr(num, zivotinje)