"""
Zadatak 3
Dvije liste jednakih duljina možemo skalarno množiti tako da zbrajamo umnoške elemenata s istim
indeksima. Ako su liste zadane a = [𝑎1, 𝑎2, … , 𝑎𝑛] i b = [𝑏1, 𝑏2, … , 𝑏𝑛],tada je skalarni
produkt ovih dviju lista dan sa a·b = 𝑎1 · 𝑏1 + 𝑎2 · 𝑏2 + ⋯ + 𝑎𝑛 · 𝑏𝑛. Napiši funkciju koja će za
proslijeđene liste, vratiti skalarni produkt.
"""

def funkcija(lsta, lstb):
    skal_prod = 0
    for i in range(0, len(lsta)):
        skal_prod += (lsta[i] * lstb[i])
    return skal_prod

N = int(input("Unesite veličinu lista: ")) #a i b iste velicine

lsta = []
for i in range(0, N): #unos u listu a
    x = int(input("A >> "))
    lsta.append(x)
    
lstb = []
for i in range(0, N): #unos u listu b
    x = int(input("B >> "))
    lstb.append(x)
    
print(lsta)
print(lstb)    
print(funkcija(lsta, lstb))