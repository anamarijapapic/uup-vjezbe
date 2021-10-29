#a -> x+2 (x-2)
x = 0
x = x + 2 * (x - 2)
print(x)

#b -> (x+2)(x-2)
x = 0
x = (x + 2) * (x - 2)
print(x)

#c -> +(x+2)x
x = 0
x = (x + 2) * x
print(x)

#d -> x+2 Or x == 2
x = 1
x + 2 or x == 2
print(x)

#e -> x <= 2 and x => 2
x = 0
x = x <= 2 and x >= 2
print(x)

#f -> x = 2 and x >= 2
x = 1
x = x == 2 and x >= 2
print(x)

#g -> x = 2 == x and x =! 2
x = 1
x = 2 == x and x != 2
print(x)