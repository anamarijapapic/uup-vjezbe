"""
7.	Napisati rekurzivnu proceduru koja uzima broj te ga ispisuje zrcalno. Npr. 12345 ->54321 .
"""

def rekispiszrcalno(n):
    if n == 0:
        print("")
    if n > 0:
        print(n % 10, end="")
        rekispiszrcalno(n//10)

rekispiszrcalno(12345)