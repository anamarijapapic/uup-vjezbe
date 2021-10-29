"""
9.	Napisati funkciju koja prima listu brojeva i listu stringova. 
Funkcija ispisuje samo stringove na indeksima zadanim u listi brojeva.
"""

def indeksi(brojevi, stringovi):
    for i in brojevi:
        if i >= 0 and i < len(stringovi): 
        #ovako izbjegnemo index out of range, ako je neki broj iz liste brojeva prevelik da bude indeks
        #ili negativan jednostavno ne ispisuje s njim kao indeksom jer ne ulazi u if
            print(stringovi[i])

indeksi([5, 7, 2, 4, 0], ["ab", "cd", "ef", "gh", "ij", "kl", "mn", "op"])