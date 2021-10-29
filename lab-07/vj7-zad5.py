"""
Zadatak 5
Napisati rekurzivnu funkciju koja ispisuje sve bitove nekog broja.
"""

def bitovno(n):
    if n > 1:
        bitovno(n >> 1)
    print(n & 1, end="")
    
broj = int(input("Unesite broj: "))
print(bin(broj))

bitovno(broj)
