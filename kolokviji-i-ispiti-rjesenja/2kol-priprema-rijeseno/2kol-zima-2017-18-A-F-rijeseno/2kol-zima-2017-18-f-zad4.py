"""
2. Kolokvij Zima 2017-18 F

4. Napisati funkciju koja prima rjecnik koji kao kljuceve ima brojeve, a kao
vrijednosti liste brojeva. Funkcija vraca True ako je svaki kljuc jednak
zbroju pridružene liste.
"""

def zbrojlst(rj):
    zbroj = [] #pomocna lista u koju cemo spremati zbrojeve
    for k in rj:
        zbr = 0
        for e in rj[k]:
            zbr += e
        zbroj.append(zbr)
    cnt = 0 #brojac koliko je kljuceva bilo jednako zbroju pridruzene liste
    for k in rj:
        for i in zbroj:
            if k == i: #podudaranje kljuca i zbroja liste
                cnt += 1
    if cnt == len(rj):
        #ako su svi kljucevi (onoliko ih ima koliko je "dug" rjecnik) 
        #bili jednaki zbroju pridruzene liste onda je True
        return True
    return False 
                
    

rjecnik = {10: [1, 1, 6, 2], 50: [30, 20], 25: [12, 11, 2]}
rjecnik2 = {40: [10, 30], 6: [5, 5, 8], 24: [9, 8, 7]}

print(zbrojlst(rjecnik))
print(zbrojlst(rjecnik2))