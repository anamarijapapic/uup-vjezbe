"""
1. kolokvij zima 2018-2019 G

2. Napisati program koji zvjezdicama ispisuje dva kvadrata. Kvadrati su
postavljeni dijagonalno (gore-lijevo i dolje-desno). Dužinu stranice kvadrata
zadaje korisnik.
"""
"""
  0123
0 ****
1 *  *
2 *  *
3 ********
4     *  *
5     *  *
6     ****
"""
    
N = int(input("Unesite duzinu stranice kvadrata: "))

for y in range(N):
    for x in range(N):
        if y == 0: # gornja crta
            print("*", end="")
        elif x == 0 or x == N-1: # lijeva i desna crta gornjeg
            print("*", end="")
        else:
            print(" ", end="")
    print("")
    
for y in range (N):
    for x in range(2*N): # srednja crta
        if y == 0:
            print("*", end="")
        elif x == N or x == (2*N)-1: # lijeva i desna crta donjeg
            print("*", end="")
        else:
            print(" ", end="")
    print("")
    
for y in range(2*N): # donja crta
        if y >= N and y <= 2*N:
            print("*", end="")
        else:
            print(" ", end="")
 