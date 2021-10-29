"""
1. kolokvij zima 2018-2019 B

4. Napisati funkciju koja prima dvije 2D koordinate kao parove pozitivnih
cijelih brojeva. Funkcija vraca vecu 2D koordinatu (onu ciji je zbroj x i y
koordinate veci).
"""

def vecakoordinata(k1, k2):
    x1, y1 = k1
    x2, y2 = k2
    if x1 + y1 > x2 + y2:
        return k1
    elif x1 + y1 < x2 + y2:
        return k2
    else:
        return ("Koordinate su jednake.")

a1 = (4, 6)
a2 = (7, 9)
print(vecakoordinata(a1, a2))
print(vecakoordinata((2, 3), (4, 5)))
print(vecakoordinata((8, 1), (8, 1)))
