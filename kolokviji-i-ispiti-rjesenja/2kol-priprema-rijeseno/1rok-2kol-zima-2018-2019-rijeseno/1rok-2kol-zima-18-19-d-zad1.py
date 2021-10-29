"""
1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) D

1. Napisati funkciju koja prima listu brojeva i ispisuje samo parne elemente.
"""

def parniel(lst):
    for el in lst:
        if el % 2 == 0:
            print(el, end=" ")

parniel([7, 8, 5, 3, 3, 6, 2, 1, 4])