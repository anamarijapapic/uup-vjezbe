"""
2.	Napisati funkciju koja prima dva broja sa jednakim brojem znamenki. 
Funkcija vraća koliko je znamenki prvog broja veće od znamenki drugog broja. 
"""

def brvecihznam(a, b):
    brojac = 0
    while a > 0 or b > 0:
        if a % 10 > b % 10:
            brojac += 1
        a //= 10
        b //= 10
    return brojac
            
print(brvecihznam(9637, 5410))
print(brvecihznam(2, 6))
print(brvecihznam(222, 222))
print(brvecihznam(763210584, 845632107))