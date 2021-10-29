"""
Zadatak 4
Napisati rekurzivnu funkciju koja prima kao parametar pozitivan cijeli broj i 
vraća zbroj svih parnih brojeva do tog broja.
"""

def zbrojiparne(n):
    #osnovni slucaj
    if n == 0:
        return 0
    
    #ako je neparan smanjujemo ga za jedan da postane paran
    if n % 2 == 1:
        n = n - 1
        
    #rekurzivni slucaj
    #od najveceg n do 0, silazni korak -2 jer smo osigurali da je paran i zelimo i dalje parne
    return n + zbrojiparne(n - 2)
        

broj = int(input("Unesite pozitivan cijeli broj: "))
print(zbrojiparne(broj))