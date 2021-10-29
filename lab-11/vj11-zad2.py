"""
Zadatak 2
Napisati program koji od korisnika čita brojeve i sprema ih u listu. 
Kada korisnik upiše 0, program pita za dodatni broj N i ispisuje zbroj zadnjih N upisanih brojeva. 
Ako u listi nema dovoljno brojeva, program ispisuje grešku i završava.
"""

lst = []

while True:
    br = int(input("Unesite broj: "))
    lst.append(br)
    
    if br == 0:
        N = int(input("Unesite dodatni broj: "))
        if N > (len(lst)):
            print("Greska! Nema dovoljno brojeva.")
            break
        
        zbroj = 0
        while N > 0:
            zbroj += lst[-N]
            N -= 1
        if N == 0:
            print("Zbroj:", zbroj)
            break