"""
Zadatak 2
Varijablama a i b pridružiti proizvoljne cjelobrojne vrijednosti.
Napisati izraze koji provjeravaju iduće činjenice 
(izraze koji rezultiraju u True ili False kada se izvrše u interpreteru). 
Brojčane pozicije bitova brojimo od najmanje značajnog bita:
a) je li zadnji bit broja a postavljen na 1
b) je li četvrti bit broja a postavljen na 1
c) jesu li zadnja tri bita varijabli a i b jednaki
d) jesu li predzadnja tri bita varijabli a i b jednaki
e) jesu li četvrti i šesti bit broja a postavljen na 1
f) jesu li četvrti ili šesti bit broja a postavljen na 1
g) je li samo četvrti ili šesti bit broja a postavljen na 1
"""

#binarne pozicije brojimo od lsb (s desna na livo pozicije)
#tako je zadnji bit (znamenka) -> 1. mjesto -> 2^0 = 1
#predzadnji bit -> 2. mjesto -> 2^1 = 2
#3. bit -> 3. mjesto -> 2^2 = 4
#4. bit -> 4. mjesto -> 2^3 = 8
#5. bit -> 5. mjesto -> 2^4 = 16
#6. bit -> 6. mjesto -> 2^5 = 32 itd.

#za neki bit na n. mjestu (iz broja a) provjeravam je li na tom mjestu 1 na način da 
#ako *je* onda triba vrijediti a & (2^(n-1)) == 2^(n-1)
#ako provjeravam je li na više mista onda zbrajam

a = 57
b = 49
print("a = ", bin(a))
print("b = ", bin(b))

#a
if  a & 1 == 1: #jer je na 1. mjestu bit 2^0 -> 1
    print(True)
else:
    print(False)

#b
if a & 8 == 8: #jer je na 4. mjestu bit 2^3 -> 8
    print(True)
else:
    print(False)
    
#c
if a & 7 == b & 7:
    #zanimaju me 1., 2. i 3. bit -> zbrajam njihove vrijednosti 2^0 + 2^1 + 2^2 = 7
    print(True)
else:
    print(False)
    
#d
if a & 14 == b & 14:
    #zanimaju me 2., 3. i 4. bit -> zbrajam njihove vrijednosti 2^1 + 2^2 + 2^3 = 14
    print(True)
else:
    print(False)
    
#e
if a & 40 == 40: #zbrajam vrijednosti 4. i 6. mjesta -> 2^3 + 2^5 = 40
    print(True)
else:
    print(False)
    
#f
if a & 8 == 8 or a & 32 == 32: 
    #jer je na 4. mjestu bit 2^3 -> 8, a na 6. mjestu bit 2^5 -> 32
    print(True)
else:
    print(False)
    
#g
if (a & 8 == 8 and a & 32 != 32) or (a & 8 != 8 and a & 32 == 32):
    #jer je na 4. mjestu bit 2^3 -> 8, a na 6. mjestu bit 2^5 -> 32
    print(True)
else:
    print(False)

