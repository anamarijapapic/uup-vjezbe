"""
2. Kolokvij Zima 2017-18 F

3. Napisati funkciju koja primljeni string rastavlja na niz stringova. Svaki
element u nizu ce biti dio originalnog stringa koji pocinje velikim slovom
i završava tockom.
"""

def rastavi(string):
    niz = []
    i_prije = 0
    for i in range(len(string) - 1):
        if string[i] == "." and string[i + 1].isupper(): #ako je trenutni ".", a sljedeci veliko slovo
            dio = string[i_prije:i + 1] 
            #dio ide od prethodnog memoriranog indeksa do i (tako da ga ukljucuje -> i+1)
            i_prije = i + 1 #azuriramo "prethodni" polozaj
            niz.append(dio)
    dio = string[i_prije:] #ostatak stringa (od zadnje tocke i velikog slova) u niz
    niz.append(dio) #dodajemo ostatak stringa u niz
    return niz
    
print(rastavi("Učim.Za ispit.Iz programiranja.u utorak."))