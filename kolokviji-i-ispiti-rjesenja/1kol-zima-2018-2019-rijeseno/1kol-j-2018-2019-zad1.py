"""
1. kolokvij zima 2018-2019 J

1. Napisati program koji od korisnika cita visinu znaka (širina je jednaka
visini) i zvjezdicama ispisuje znak „+“.
"""

"""
    *    
    *    
    *    
    *    
*********
    *    
    *    
    *    
    *   
"""

N = int(input("Unesite visinu znaka: "))

for i in range(N):
    for j in range(N):
        if i == N//2 or j == N//2:
            print("*", end="")
        else: 
            print(" ", end="")
    print("")
