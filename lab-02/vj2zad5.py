"""
Unosimo djeljenik (pridruzen varijabli x) i djeljitelj (pridruzen varijabli y).
Dobivamo rezultat ostatka dijeljenja (pridruzen varijabli z) tako da 
dokle god je istinit uvjet da je x >= y racunamo z=x-y pa x=x-y.
Ispisujemo iznos varijable z - ostatak dijeljenja.
(Varijabla z je zapravo viska, zato je doli zakomentirano.)
"""
x=int(input("Unesite djeljenik: "))
y=int(input("Unesite djeljitelj: "))
while x>=y:
#   z=x-y
    x=x-y
print(x)


print(5%2)