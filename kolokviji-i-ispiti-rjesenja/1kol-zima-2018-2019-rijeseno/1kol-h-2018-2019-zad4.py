"""
1. kolokvij zima 2018-2019 H

4. Napisati rekurzivnu funkciju djelitelji() koja ispisuje sve djelitelje broja
333.
"""
    
def djelitelji(i):
    if i == 334:
        return
    if 333 % i == 0:
        print(i)
    djelitelji(i + 1)
    
djelitelji(1)