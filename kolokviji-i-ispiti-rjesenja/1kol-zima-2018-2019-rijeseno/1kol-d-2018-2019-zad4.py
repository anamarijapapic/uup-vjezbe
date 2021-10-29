"""
1. kolokvij zima 2018-2019 D

4. Napisati rekurzivnu funkciju koja broji koliko je bitova nekog broja postavljeno
na 1.
"""

def rekbit(broj):
    if broj == 0:
        return 0
    return (broj & 1) + rekbit(broj >> 1)

print(bin(9))
print(rekbit(9))