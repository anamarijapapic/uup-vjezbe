"""
2. Kolokvij Zima 2017-18 E

1. Napisati funkciju koja prima listu brojeva i listu booleana jednake dužine.
Lista booleana ima tocno dva elementa postavljena na True. Ta dva elementa
oznacavaju pocetak i kraj liste brojeva koju funkcija treba „izbaciti“
iz originalne liste (funkcija vraca novu listu). Na primjer, za liste [ 6, 2,
8, 4, 9 ] i [ F, T, F, T, F ], funkcija vraca listu [ 6, 9 ].
"""

def izbaci(lista, listabool):
    nova = []
    cnt = 0
    for broj, b in zip(lista, listabool): #zip() funkcija koja povezuje liste tako da su oni elementi
    #koji imaju iste indekse zajedno u skupu na tom indeksu u novoj zip listi
        if not b and cnt != 1: #ako je u listi booleana False i pod uvjetom da counter nije 1
        #(jer ako je counter 1 znaci da jos nismo dosli do drugog True)
            nova.append(broj)
        elif b:
            cnt += 1 #kad nademo True u listi booleana povecavamo counter
    return nova

print(izbaci([6, 2, 8, 4, 9], [False, True, False, True, False]))