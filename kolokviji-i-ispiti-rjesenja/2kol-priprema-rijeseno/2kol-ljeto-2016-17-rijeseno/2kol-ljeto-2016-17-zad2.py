"""
2. Kolokvij Ljeto 2016-17

2. Napisati funkciju koja prima jedan string. String može biti „X plus Y“ ili
„X minus Y“, gdje su X i Y dva cijela broja (mogu imati više znamenki
ili predznak). Funkcija vraca zbroj ili razliku brojeva X i Y.
"""

def plusminus(string):
    prvi, operacija, drugi = string.split(" ")
    X = int(prvi)
    Y = int(drugi)
    if operacija == "plus":
        return X + Y
    elif operacija == "minus":
        return X - Y

print(plusminus("52 plus 8"))
print(plusminus("58 minus 8"))