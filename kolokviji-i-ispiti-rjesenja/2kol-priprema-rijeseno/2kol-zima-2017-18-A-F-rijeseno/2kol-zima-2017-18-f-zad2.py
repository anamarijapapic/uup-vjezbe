"""
2. Kolokvij Zima 2017-18 F

2. Napisati funkciju koja prima string sastavljen od malih slova. Funkcija
vraca string gdje su svi dvostruki suglasnici zamijenjeni jednim suglasnikom.
Npr. za string "lookk", funkcija ce vratiti "look".
"""

def dvostruki_sugl(string):
    samoglasnici = ['a', 'e', 'i', 'o', 'u']
    novi_string = string[0]
    preskok = False
    for c in string[1:]: #od 1. el. jer smo 0. el. vec pridruzili u novi string jer nema prethodnika
        if c != novi_string[-1] or c in samoglasnici:
            #nisu ponovljeni i samoglasnici su -> ne zamjenjujemo ih, ostaju u stringu
            novi_string += c
            preskok = False
        elif c == novi_string[-1] and c not in samoglasnici and not preskok:
            #jednak kao i prethodni, suglasnik i nije vec preskocen
            #-> preskok = True kako sljedeceg ne bi preskakali
            preskok = True
        else:
            novi_string += c
            preskok = False
    return novi_string

print(dvostruki_sugl("lookk"))