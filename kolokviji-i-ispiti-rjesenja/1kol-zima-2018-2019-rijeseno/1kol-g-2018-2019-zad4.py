"""
1. kolokvij zima 2018-2019 G

4. Napisati rekurzivnu funkciju koja prima dva broja i vraca koliko se znamenki
brojeva razlikuju. Na primjer za brojeve 36415 i 32816, funkcija
vraca 3.
"""

def razlikuju(x, y):
    if x == 0 or y == 0:
        return 0
    return (x % 10 != y % 10) + razlikuju(x//10, y//10)

print(razlikuju(36415, 32816))
print(razlikuju(555, 555))
print(razlikuju(146, 456))