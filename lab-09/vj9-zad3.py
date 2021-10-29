"""
Zadatak 3
Napisati funkciju koja prima listu brojeva i vraća dva booleana. 
Prvi boolean je True samo ako su sve vrijednosti u listi jednake, 
drugi boolean je True samo ako su barem dvije vrijednosti u listi jednake.
"""

def jedvrijednosti(lst):
    for e in lst:
        brojac = 0
        for el in lst:
            if e == el:
                brojac += 1 # postoji vec element iste vrijednosti u listi
        if brojac == len(lst):
                return True, True # brojac jednak duzini liste (broju el. liste) --> svi clanovi jednaki
        elif brojac >= 2: # nadeno je 2 ili vise istih elemenata u listi
                return False, True
    return False, False

def sve_bardva(lst): # samo pomoc za ispis
    sve, bardva = jedvrijednosti(lst) # varijable preuzimaju boolean vrijednosti
    if sve:
        print("Sve vrijednosti u listi su jednake.")
    elif bardva:
        print("Barem dvije vrijednosti u listi su jednake.")
    else:
        print("Ne postoje jednake vrijednosti u listi.")

lst1 = [8, 9, 40, 23, 86, 12, 7, 40]
lst2 = [8, 40, 40, 23, 40, 12, 7, 40]
lst3 = [8, 9, 55, 23, 86, 12, 7, 40]
lst4 = [5, 5, 5, 5, 5]

sve_bardva(lst1)
sve_bardva(lst2)
sve_bardva(lst3)
sve_bardva(lst4)