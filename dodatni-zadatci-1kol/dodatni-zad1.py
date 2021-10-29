"""
1.	Napisati funkciju koja čita dva po dva broja dok god korisnik ne upiše jedan 
negativni i jedan pozitivni broj. Funkcija nakon toga vraća ta dva broja.
"""

def dvapodva():
    while True:
        prvi = int(input("Unesite prvi broj: "))
        drugi = int(input("Unesite drugi broj: "))
        prethprvi = prvi
        prethdrugi = drugi
        if (prethprvi < 0 and prethdrugi > 0) or (prethprvi > 0 and prethdrugi < 0):
            return prethprvi, prethdrugi
            
print(dvapodva())