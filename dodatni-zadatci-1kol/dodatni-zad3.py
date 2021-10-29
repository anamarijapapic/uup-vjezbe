"""
3.	Napisati funkciju koja čita dva po dva broja dok god korisnik ne unese dva broja 
koja su oba veća od prethodna dva broja. Funkcija nakon toga vraća ta dva broja. 
Prva dva unesena broja se ne vraćaju. 
"""

def dvapodva():
    a = int(input("Prvi broj: "))
    b = int(input("Drugi broj: "))
    pretha = a
    prethb = b
    while True:
        a = int(input("Prvi broj: "))
        b = int(input("Drugi broj: "))
        if a > pretha and b > prethb:
            return a, b
        pretha = a
        prethb = b

print(dvapodva())