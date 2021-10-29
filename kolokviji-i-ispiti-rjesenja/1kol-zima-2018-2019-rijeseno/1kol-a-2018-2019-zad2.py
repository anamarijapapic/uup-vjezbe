"""
1. kolokvij zima 2018-2019 A

2. Napisati funkciju koja za tri primljena broja vraca najvecu razliku izmeu
dvoje od njih. Na primjer za 3, 8 i 2, funkcija vraca 6.
"""

def maxrazlika (a, b, c):
    if a >= b and a >= c: 
        najveci = a
    elif b >= a and b >=c:
        najveci = b
    else:
        najveci = c
    if a <= b and a <= c:
        najmanji = a
    elif b <=a and b <= c:
        najmanji = b
    else:
        najmanji = c
    return najveci - najmanji

print(maxrazlika(3, 8, 2))
