a = 2
b = 3

#a
if a > 0 and b > 0:
    print("a i b su pozitivni")
else:
    print("a i b nisu pozitivni")

#b
if a % 2 == 0 or b % 2 == 0:
    print("jedan od brojeva ili oba su parni")
else:
    print("nijedan od brojeva nije paran")

#c
if (a % 2 == 0 and b % 2 == 0) and a > b:
    print("oba broja su parna i a je veci od b")
else:
    print("nisu i oba broja parna i a veci b")

#d
if a % 2 != 0 or b % 2 != 0:
    print("barem jedan od a i b je neparan")
else:
    print("oba broja su parna")

#e
if a % 2 != 0 and b % 2 != 0: 
    print("oba su neparna ili oba parna")
else:
    print("najvise jedan od a i b je neparan")

#f
if a % b == 0 and b % a == 0:
    print("a je djeljiv sa b i obrnuto")
elif a % b == 0:
    print("a je djeljiv sa b ")
elif b % a == 0:
    print("b je djeljiv sa a")
else:
    print("a i b nisu medusobno djeljivi")

#g
if a % b == 0 and b % a != 0:
    print("a je djeljiv sa b, a b nije djeljiv sa a")
else:
    print("False")