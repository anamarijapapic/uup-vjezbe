"""
7.	Napisati funkciju koja prima broj N i vraća dijagonalnu matricu veličine NxN.
"""

def dijagmat(N):
    matrica = []
    for i in range(N):
        redak = []
        #dijagonalna -> vrijednosti samo na dijagonali, ostalo 0
        for j in range(N):
            if i == j: #gradimo npr jedinicnu dijag. matricu pa na dijagonalu postavljamo 1
                redak.append(1)
            else:
                redak.append(0) #ono sto nije na dijagonali je 0
        matrica.append(redak)
    return matrica

N = int(input("Unesite zeljenu velicinu matrice: "))

mat = dijagmat(N)
for red in mat: #samo radi lipseg ispisa matrice, inace je kao lista
    print(red)