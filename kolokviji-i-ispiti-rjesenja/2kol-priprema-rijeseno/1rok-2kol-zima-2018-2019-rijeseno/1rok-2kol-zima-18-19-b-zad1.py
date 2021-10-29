"""
1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) B

1. Napisati funkciju koja prima listu brojeva i ispisuje samo elemente na
parnim indeksima.
"""

def parni(lst):
    for i in range(len(lst)):
        if i % 2 == 0:
            print(lst[i], end=" ")

parni([1, 8, 7, 9, 2, 3, -6, 5, 0, 4])