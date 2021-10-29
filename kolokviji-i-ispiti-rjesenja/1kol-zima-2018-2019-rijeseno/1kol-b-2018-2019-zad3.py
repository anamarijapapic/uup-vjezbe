"""
1. kolokvij zima 2018-2019 B

3. Napisati program koji u beskonacnoj petlji ispisuje proste brojeve. Program
se oslanja na funkciju prost() (napisati je).
"""

def prost(a):
    if a == 0 or a == 1:
        return False
    if a == 2:
        return True
    for i in range (2, a):
        if a % i == 0:
            return False
        else:
            return True
    
i = 0
while i >= 0:
    if prost(i):
        print(i)
    i += 1