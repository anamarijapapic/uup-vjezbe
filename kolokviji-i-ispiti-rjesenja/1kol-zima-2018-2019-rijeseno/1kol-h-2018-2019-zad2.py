"""
1. kolokvij zima 2018-2019 H

2. Napisati program koji od korisnika cita (neparnu) visinu znaka i zvjezdicama
ispisuje broj 3 (kao na digitronu).
"""

"""
*****
    *
*****
    *
*****    
"""

N = int(input("Unesite visinu znaka (neparnu): "))

for i in range(N):
    for j in range(N):    
        if i == 0 or i == N//2 or i == N-1: # 3 vodoravne crte
            print("*", end="")
        else:
            if j == N-1: # okomita crta na kraju
                print("*", end="")
            else:
                print(" ", end="")
    print("")