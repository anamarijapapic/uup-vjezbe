"""
1. kolokvij zima 2018-2019 I

1. Napisati program koji od korisnika cita visinu broja i zvjezdicama ispisuje
broj 8 (kao na digitronu).
"""

"""
****
*  *
****
*  *
****
"""

l = int(input("Unesite visinu: "))

for i in range(l):
    for j in range(l):
        if i == 0 or i == l//2 or i == l-1:
            print("*", end="")
        else:
            if j == 0 or j == l-1:
                print("*", end="")
            else:
                print(" ", end="")
    print("")
