"""
1. kolokvij zima 2018-2019 A

1. Napisati program koji od korisnika cita dužinu katete i zvjezdicama ispisuje
ispunjeni pravokutan trokut (katete su postavljene kao L).
"""

# *
# **
# ***
# ****
# *****

N = int(input("Unesite duzinu katete pravokutnog trokuta: "))

for i in range (N):
    for j in range (N):
        if i >= j:
            print("*", end="")
    print("")
