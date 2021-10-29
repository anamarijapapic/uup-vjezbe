"""
Zadatak 3
Napisati program koji broji koliko je bitova broja (od zadnjih 32 bita) postavljeno na 1.
"""
#pozicije se broje s desna na lijevo -> 1. mjesto: 2^0, 2. mjesto 2^1, 3. mjesto 2^2 itd.
#za neki bit na n. mjestu (iz broja x) provjeravam je li na tom mjestu 1 na način da 
#ako *je* onda triba vrijediti x & (2^(n-1)) == 2^(n-1)

x = int(input("Unesite broj: "))
print("x = ", bin(x))

brojac = 0

for i in range (0, 32):
   if x & 2**i == 2**i:
       brojac += 1
       
print("Broj bitova postavljenih na 1 (od zadnja 32 bita): ", brojac)