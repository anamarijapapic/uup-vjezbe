"""
1. kolokvij zima 2018-2019 C

4. Napisati funkciju koja prima dva broja. Funkcija ispisuje sve brojeve do
1000 koji dijele oba primljena broja.
"""

def ispis(x, y):
    for i in range (1, 1001):
        if i % x == 0 and i % y == 0:
            print(i)
            
ispis(100, 16)
