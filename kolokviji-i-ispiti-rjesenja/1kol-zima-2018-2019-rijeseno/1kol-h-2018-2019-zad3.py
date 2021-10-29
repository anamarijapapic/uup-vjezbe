"""
1. kolokvij zima 2018-2019 H

3. Napisati program koji zvjezdicama iscrtava trokut s vrhom okrenutim
prema dolje. Visinu trokuta zadaje korisnik. Zadatak rješiti petljama
i pomocnim funkcijama za iscrtavanje N razmaka i za iscrtavanje N zvjezdica.
"""

"""
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
"""

N = int(input("Unesite visinu trokuta: "))
            
for r in range(N):
    for s in range(N):
        if r <= s or s == N-1 or r == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
    
print("")
    
for r in range(N):
    for s in range(N):
        if s <= N - r - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")