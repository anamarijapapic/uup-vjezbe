#a
x = 0
x = 6
y = 1
x = y

'''
  File "C:/Users/User/Desktop/Anamarija Papic/vj3-3.py", line 4, in <module>
    x = y

NameError: name 'y' is not defined
'''
# varijabla y nije inicijalizirana/deklarirana
# inicijalizirat cemo varijablu y tako da joj zadamo vrijednost 1
# sada mozemo varijabli x pridruziti vrijednost y

#b
y = 1
x = y + 2

'''
  File "C:/Users/User/Desktop/Anamarija Papic/vj3-3.py", line 19, in <module>
    x = y + 2

NameError: name 'y' is not defined
'''
# varijabla y nije inicijalizirana/deklarirana kao i u proslom zadatku
# inicijalizirat cemo varijablu y tako da joj zadamo vrijednost npr. 1
# sada mozemo varijabli x pridruziti vrijednost y + 2

#c
x = 5
y = 1
x = (x/2) + (2/y)

'''
  File "C:/Users/User/Desktop/Anamarija Papic/vj3-3.py", line 33, in <module>
    x = (x/2) + (2/y)

ZeroDivisionError: division by zero
'''
# Python ne dopusta dijeljenje s nulom jer cemo dobiti zero division error
# to cemo popraviti tako da varijabli y koja iznosi 0 i s kojom ujedno
# zelimo dijeliti promijenimo vrijednost npr. zadamo y = 1