"""
Zadatak 3
Napisati iterativnu i rekurzivnu verziju funkcije za ispis broja u heksadecimalnom obliku (baza 16). 
Napisati pomoćnu funkciju koja će umjesto broja 10, 11, .. 15 ispisati odgovarajuće slovo 'A', 'B' .. 'F'.
"""

def slovo(x): #print odgovarajuceg slova/znamenke
    if x == 10:
        x = 'A'
    elif x == 11:
        x = 'B'
    elif x == 12:
        x = 'C'
    elif x == 13:
        x = 'D'
    elif x == 14:
        x ='E'
    elif x == 15:
        x = 'F'
    print(x, end="")
        
def heks(n): # iteretivna -> obrnuti redoslijed ispisa znamenki
    while n > 0:
        slovo(n % 16) # n % 16 je ostatak --> odnosno znamenke
        n //= 16 # kidamo broj
    print()

def rekheks(n): # rekurzivna -> stvaran redoslijed ispisa znamenki
    if n == 0:
        return
    rekheks(n // 16)
    slovo(n % 16)
        
dekad = int(input("Unesite broj: "))
heks(dekad)
rekheks(dekad)