"""
8.	Napisati funkciju koja prima jedan string i dva broja A i B. 
Funkcija vraća true ako prvi string sadrži A samoglasnika i B suglasnika. 
Npr. za string „ab cd e“, A=2 i B=3, funkcija vraca True.
"""

def samoglsugl(string, A, B):
    samogl = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    brsamogl = 0
    brsugl = 0
    for c in string:
        if c in samogl:
            brsamogl += 1
        elif c.isalpha() and c not in samogl:
            brsugl += 1
    if brsamogl == A and brsugl == B:
        return True
    return False
            

print(samoglsugl("ab cd e", 2, 3))