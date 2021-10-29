"""
2. Kolokvij Zima 2017-18 D

1. Napisati funkciju koja prima listu brojeva i ispisuje samo elemente na
parnim indeksima.
"""

def parniind(lst):
    for i in range(len(lst)):
        if i % 2 == 0:
            print(lst[i])
            
parniind([8, 4, 2, 5, 7, 6, 3, 1, 9])