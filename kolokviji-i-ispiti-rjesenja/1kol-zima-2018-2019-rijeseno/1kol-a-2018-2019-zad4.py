"""
1. kolokvij zima 2018-2019 A

4. Napisati funkciju skrati(). Funkcija prima brojnik i nazivnik razlomka i
vraca ih skracene (podijeljene sa najvecim zajednickim djeliteljem).
"""

brojnik = int(input("Brojnik razlomka: "))
nazivnik = int(input("Nazivnik razlomka: "))

def najvzajdj(a, b):
    if a == b:
        return a
    elif a > b:
        return najvzajdj(a - b, b)
    else:
        return najvzajdj(a, b - a)

def skrati(br, naz):
    dj = najvzajdj(br, naz)
    return (br // dj, naz // dj)

skracbrojnik, skracnazivnik = skrati(brojnik, nazivnik)
print("Skraceni razlomak je: ", skracbrojnik, "/", skracnazivnik)