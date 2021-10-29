"""
2. Kolokvij Zima 2017-18 E

3. Napisati funkciju koja prima matricu (listu lista) i vraca listu sastavljenu
od svih brojeva u matrici.
"""

def izmatrice(mat):
    brojevi = []
    for el in mat:
        for i in el:
            if i not in brojevi:
                brojevi.append(i)
    return brojevi

matrica = [[1, 2, 3, 4], 
           [2, 4, 6, 8], 
           [10, 20, 50, 30], 
           [1, 0, 5, 7]]

print(izmatrice(matrica))