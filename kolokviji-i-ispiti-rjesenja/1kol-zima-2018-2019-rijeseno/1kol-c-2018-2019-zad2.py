"""
1. kolokvij zima 2018-2019 C

2. Napisati funkciju skrati(). Funkcija prima brojnik i nazivnik razlomka i
vraca ih skracene (podijeljene sa najvecim zajednickim djeliteljem).
"""

def skrati(br, naz):
    if br >= naz:
        veci = br
    if naz > br:
        veci = naz
    for i in range(veci, 1, -1):
        if br % i == 0 and naz % i == 0:
            br //= i
            naz //= i
    return br, naz

brojnik = int(input("Unesite brojnik: "))
nazivnik = int(input("Unesite nazivnik: "))

skracbrojnik, skracnazivnik = skrati(brojnik, nazivnik)
print("Skraceni razlomak je: ", skracbrojnik, "/", skracnazivnik)