"""
Zadatak 4
Napisati funkciju koja prima listu stringova i vraća novu listu stringova. 
U novu listu se dodaju samo stringovi koji su ispravni e-mailovi po formatu 'ime.prezime@unist.hr', 
gdje su ime i prezime dugi do 10 znakova.
"""

def vracanje(lst):
    novalst = []
    for e in lst:
        popola = e.split('@')
        if len(popola) == 2 and popola[1] =="unist.hr":
               prvi_dio = popola[0].split(".")
               flag = True
        else:
            flag = False
        if flag and (len(prvi_dio[0]) < 10 and len(prvi_dio[1]) < 10 ):
            if (prvi_dio[0].isalpha() and prvi_dio[1].isalpha()):
                novalst.append(e)
    return novalst

mailovi=[ "anamarija.papic@unist.hr", "imeprezime@unist.hr", "ime.prezime@unist.hr", "ime.prezime@@oss.unist.hr", "ime.prezime@oss@unist.hr"]
print(vracanje(mailovi))