"""
1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) A

1. Napisati program koji od korisnika cita brojeve i sprema ih u listu. Kada
korisnik upiše 0, program pita za dodatni broj N i ispisuje zbroj zadnjih
N upisanih brojeva. Ako u listi nema dovoljno brojeva, program ispisuje
grešku i završava.
"""

lst = []
zbroj = 0

while True:
    br = int(input("Unesite broj koji zelite unijeti u listu: "))
    lst.append(br)
    if br == 0:
        N = int(input("Upisite dodatni broj N: "))
        if N > len(lst):
            print("Greska! Nema dovoljno brojeva u listi.")
        else:
            for i in range(len(lst) - N, len(lst)):
                zbroj += lst[i]
            print("Zbroj zadnjih", N, "upisanih brojeva: ", zbroj)
        break