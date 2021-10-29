"""
1. kolokvij zima 2018-2019 I

3. Napisati funkciju koja prima 2D koordinatu kao par pozitivnih cijelih
brojeva. Funkcija ispisuje sve koordinate izmeu (0,0) i te koordinate.
Na primjer, za (2,3) ispisuje (0,0), (0,1), (0,2), (1,0), (1,1) i (1,2).
"""

def izmedukoor(k):
    x, y = k
    for i in range(x):
        for j in range(y):
            izmeduk = (i, j)
            print(izmeduk)

koordinata = (2,3)
izmedukoor(koordinata)

#kx=(int(input()), int(input()))
#print(kx)