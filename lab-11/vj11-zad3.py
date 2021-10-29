"""
Zadatak 3
Napisati funkciju koja prima listu brojeva i vraća listu booleana. 
Svaki element u listi booleana (osim prvog) će odgovarati jednom elementu u listi brojeva. 
Element će biti True ako je broj na istom indeksu veći od broja na prethodnom indeksu.
"""

def boolean(brojevi):
    lista = [True] #prvi broj -> zadan kao True (nema prethodnika)
    
    for i in range(len(brojevi)-1):
        if brojevi[i+1] > brojevi[i]: #usporedba za True -> trenutni veci od prethodnog
            lista.append(True)
        else:
            lista.append(False)
    return lista

num = [1, 2, 10, 6, 0, 4, 8]
print(boolean(num))