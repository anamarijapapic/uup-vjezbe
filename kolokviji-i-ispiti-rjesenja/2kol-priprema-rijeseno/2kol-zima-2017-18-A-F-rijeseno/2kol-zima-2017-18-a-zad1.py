"""
2. Kolokvij Zima 2017-18 A

1. Napisati funkciju koja prima dvije liste brojeva. Funkcija vraca listu sa
brojevima koji se pojavljuju u prvoj, ali ne i u drugoj listi. Npr. za liste [
6, 2, 7, 9 ] i [2, 4, 5, 7], funkcija vraca listu [6, 9].
"""

def neuobe(lst1, lst2):
    povrat = []
    for e in lst1:
        if e not in lst2:
            povrat.append(e)
    return povrat

lsta = [6, 2, 7, 9]
lstb = [2, 4, 5, 7]

print(neuobe(lsta, lstb))