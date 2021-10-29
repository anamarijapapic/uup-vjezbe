"""
1. kolokvij zima 2018-2019 D

2. Napisati program koji ispisuje brojeve od 1 do 1000 s tim da umjesto
svakog broja djeljivog sa 3 ispisuje „fizz“, umjesto svakog broja djeljivog
sa 5 ispisuje „buzz“, a umjesto svakog broja djeljivog sa 5 i 3 ispisuje
„fizz-buzz“.
"""

for i in range (1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print("fizz-buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)