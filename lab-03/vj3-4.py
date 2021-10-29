#a
x = 5
y = 3
z = (x / 2) + (y / 2)
#ocekuje se 4

# racunsku operaciju koju zelimo izvesti nismo nigdje pohranili
# zato cemo je pridruziti npr. varijabli z
# u Variable expolreru stvarno i vidimo da z iznosi 4.0 i tipa float je

#b
x = 5
y = x + 5
z = (x + y) % 2
#ocekuje se 1

# racunsku operaciju koju zelimo izvesti nismo nigdje pohranili
# zato cemo je pridruziti npr varijabli z
# dodali smo zagrade koje su nedostajale kako bismo dobili ispravan rezultat
# tj. (x + y) % 2 == 1 (radi se o ostatku cijelobrojnog dijeljenja)

#c
x = 1234
#ocekuju se ispisi 1, 2, 3 i 4
print(x // 1000)
print(x // 100 % 10)
x = x // 10
print(x % 10)
x  = 1234
print(x % 10)

# prvo se nista ne ispisuje jer nemamo naredbi print
# print(x // 1000) ispisuje 1 (radi se o cijelobrojnom dijeljenju)
# print(x // 100 % 10) ispisuje 2 
# (prvo cijelobrojno dijelimo sa 100 -> dobivamo 12)
# (onda od 12 dobivamo ostatak cijelobrojnog dijeljenja s 10 -> 2)
# x = x // 10 -> sada x iznosi 123 zbog cijelobrojnog dijeljenja s 10
# print(x % 10) ispisuje 3 jer 123 % 10 = 3 (ostatak cijelobrojnog dijeljenja)
# x  = 1234 ovdje opet zadamo koliko iznosi x jer smo prije izgubili 4 kao znamenku jedinica
# print(x % 10) ispisuje 4 jer ostatak dijeljenja 1234 s 10 je 4