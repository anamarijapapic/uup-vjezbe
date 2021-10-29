"""
2. Kolokvij Zima 2017-18 A

3. Napisati funkciju koja prima paran broj N i vraca matricu velicine NxN
ispunjenu sa jedinicama i nulama. Gornja polovica matrice je ispunjena
jedinicama.
"""

def gorematrica(N):
    mat = []
    for i in range(N):
        redak = []
        for j in range(N):
            if i < j:
                redak.append(1)
            else:
                redak.append(0)
        mat.append(redak)
    return mat
    
m = gorematrica(6)
for r in m:
    print(r)