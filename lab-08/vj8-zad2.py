"""
Zadatak 2
Napisati funkciju koja pretvara 3D koordinatu u 2D koordinatu. 
Koordinate su predstavljene trojkom ili parom decimalnih brojeva. 
Funkcija prima 3D koordinatu kao parametar i vraća 2D koordinatu. 
Funkcija pretvara koordinate iz 3D u 2D tako da od 3D koordinate uzme dvije najmanje vrijednosti.
"""

def tridudvad(k):
    x, y, z = k
    if x >= y and x >= z:
        return y, z
    elif y >= x and y >= z:
        return x, z
    else:
        return x, y

koordinata1 = (8, 9, 1)
koordinata2 = (0, 5, -10)
koordinata3 = (7, 7, 7)
print(tridudvad(koordinata1))
print(tridudvad(koordinata2))
print(tridudvad(koordinata3))