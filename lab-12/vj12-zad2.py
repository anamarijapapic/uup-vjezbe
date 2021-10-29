"""
Zadatak 2
Napiši funkciju koja će za dva ulazna parametra prirodan broj n i listu od n elemenata, ispisati elemente
te liste zdesna prema lijevo (posljednje uneseni element ispisuje se prvi). Korisnik unosi prirodan broj
n i listu elemenata. Funkcija nema povratne vrijednosti.
"""

def funkcija(lst, n):
     for el in lst[::-1][:n]: 
         #[::-1] predznak minus obrne listu, ispisujemo od prvog el. obrnute liste (zadnjeg el. normalne)
         #[:n] ispisujemo do n-tog zadanog elementa 
         print(el)

lista = [7, 9, 8, 3, 4]
br = 5

funkcija(lista, br)