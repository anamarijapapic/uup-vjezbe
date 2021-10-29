"""
2. Kolokvij Zima 2017-18 D

3. Napisati funkciju koja prima listu stringova i vraca novu listu stringova. U
novu listu se dodaju samo stringovi koji su ispravni e-mailovi po formatu
’ime.prezime@unist.hr’, gdje su ime i prezime dugi do 10 znakova.
"""

def primi_vrati(lst):
    ispravni = []
    for e in lst:
        dijelovi = e.split("@") #rastavljanje na ime.prezime i domenu
        if len(dijelovi) == 2 and dijelovi[1] == "unist.hr":
            ime_prezime = dijelovi[0].split(".") # rastavljanje na ime i prezime posebno
            flag = True
        else:
            flag = False
        if flag and (len(ime_prezime[0]) + len(ime_prezime[1])) < 10: #ime i prezime skupa do 10 znakova
            if ime_prezime[0].isalpha() and ime_prezime[1].isalpha(): #ime i prezime iskljucivo od slova
                ispravni.append(e)
    return ispravni
                    
mailovi = ["anamarija.papic@unist.hr", "ime.prezime@unist.hr", "ime.prezime@oss@unist.hr", 
           "ana.anic@unist.hr", "petar.petric@gmail.com", "ante.antic@unist.hr", "ivan.ivic@unist.hr", 
           "mia.mijic@unist.hr", "leo.leic8@unist.hr"]

print(primi_vrati(mailovi))