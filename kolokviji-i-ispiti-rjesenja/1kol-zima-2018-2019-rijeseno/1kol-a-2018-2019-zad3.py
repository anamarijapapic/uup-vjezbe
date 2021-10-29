"""
1. kolokvij zima 2018-2019 A

3. Napisati funkciju koja cita tri po tri broja dok god korisnik ne unese dva
pozitivna broja i nulu u bilo kojem redoslijedu. Funkcija nakon toga vraca
ta tri broja.
"""

def tribroja():
    pokret = 1
    while pokret != 0:
        a = int(input("Prvi broj: "))
        b = int(input("Drugi broj: "))
        c = int(input("Treci broj: "))
        if a == 0 and b > 0 and c > 0:
            pokret == 0
            return (a, b, c)
        elif b == 0 and a > 0 and c > 0:
            pokret == 0
            return (a, b, c)
        elif c == 0 and a > 0 and b > 0:
            pokret == 0
            return (a, b, c)
        
print(tribroja())
        
