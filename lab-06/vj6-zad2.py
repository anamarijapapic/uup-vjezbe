"""
Zadatak 2
Napisati program koji kao unos prima jedan broj. 
Program iscrtava zvjezdicama slovo H dužine i visine zadane unesenim brojem.
"""

# *   *
# *   *
# *****
# *   *
# *   *

dim = int(input("Unesite dimenziju: "))

for i in range(dim // 2): #cjelobrojno djeljenje s 2 jer crtamo gornju polovicu H
    print("*", end = '')
    for j in range(dim - 2): #dim - 2 jer oduzimamo mista koja zauzimaju * na pocetku i na kraju reda
        print("-", end = "")
    print("*")
# *   *
# *   *
    
for i in range(dim):
    print("*", end = '')
print() #prelezak u novi red
# *****

for i in range(dim // 2): #cjelobrojno djeljenje s 2 jer crtamo donju polovicu H
    print("*", end = '')
    for j in range(dim - 2): #dim - 2 jer oduzimamo mista koja zauzimaju * na pocetku i na kraju reda
        print("-", end = "")
    print("*")
# *   *
# *   *

