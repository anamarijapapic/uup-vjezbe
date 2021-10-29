"""
2. Kolokvij Zima 2017-18 A

2. Napisati funkciju koja prima dva stringa i broj N. Funkcija vraca true ako
prvi string sadrži N samoglasnika, a drugi string N suglasnika. Npr. za
stringove „uzeti“, „abcde“ i N=3, funkcija vraca True.
"""

def samosugl(str1, str2, N):
    samoglasnici = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    brsam = 0
    brsug = 0
    for c in str1:
        if c in samoglasnici:
            brsam += 1
    for c in str2:
        if c not in samoglasnici and c.isalpha():
            brsug += 1
    if brsam == N and brsug == N:
        return True
    return False

print(samosugl("uzeti", "abcde", 3))