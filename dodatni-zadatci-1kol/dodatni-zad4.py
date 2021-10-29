"""
4.	Napisati rekurzivnu funkciju koja prima dva broja i vraća koliko se znamenki brojeva razlikuju. 
Na primjer za brojeve 36415 i 32816, funkcija vraća 3.
"""

def rekrazlikuju(a, b):
    brojac = 0
    if a == 0 or b == 0:
        return 0
    if a % 10 != b % 10:
        brojac += 1
    return brojac + rekrazlikuju(a//10, b//10)

print(rekrazlikuju(36415, 32816))
print(rekrazlikuju(826, 626))
print(rekrazlikuju(41578, 99566))