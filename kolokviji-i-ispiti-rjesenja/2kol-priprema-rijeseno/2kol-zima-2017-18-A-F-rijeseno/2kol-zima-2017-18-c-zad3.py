"""
2. Kolokvij Zima 2017-18 C

3. Napisati funkciju koja primljeni string rastavlja na niz stringova. Svaki
element u nizu ce biti dio originalnog stringa koji pocinje otvorenom i
završava zatvorenom zagradom. Npr. za string "ab(cd)ef(g)", funkcija
vraca [ "cd", "g" ].
"""

def rastavi(string):
    niz = []
    poc = -1
    cilj = -1
    for i in range(len(string)):
        if string[i] == "(":
            poc = i+1
        elif string[i] == ")":
            cilj = i-1
            niz.append(string[poc:cilj+1])
    return niz

print(rastavi("ab(cd)ef(g)"))