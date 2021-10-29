"""
1. kolokvij zima 2018-2019 E

1. Napisati program koji od korisnika cita dva po dva broja. Program za
svaka dva broja ispisuje sve brojeve izmeu njih.
"""

while True:
    a = int(input("Unesite prvi broj: "))
    b = int(input("Unesite drugi broj: "))
    if a < b:
        for i in range (a+1, b):
            print(i)
    elif a > b:
        for i in range (a-1, b, -1):
            print(i)
            