"""
1. kolokvij zima 2018-2019 E

4. Napisati rekurzivnu funkciju koja vraca zbroj svih znamenaka broja.
"""

def zbrojznam(n):
    if n == 0:
        return 0
    z = n % 10
    return z + zbrojznam(n // 10)

print(zbrojznam(5893118))