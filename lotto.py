import random
import re

class Lotto():
    def __init__(self,jelolesek,osszesszam,mennyithuzni):
        # Jelolesek:Mennyit kell kijelolni
        # osszesszam:Milyen intervallumból kell azokat kijelölni
        # mennyithuzni: Mennyi számot kell kihúzni
        self.jelolesek=jelolesek
        self.osszesszam=osszesszam
        self.mennyithuzni=mennyithuzni
        # Valasztott:A felhasználó által választott,vagy a gép által generált számsorozat
        # Eredmény: A lottóhúzás végeredménye
        self.__valasztott=set([])
        self.__eredmeny = set([])

    def lottohuzas(self):

        while len(self.eredmeny)<self.jelolesek:
            self.eredmeny.add(random.randint(1,self.osszesszam))
        return self.eredmeny


    def hanyjo(self):
        szam=0
        for x in self.eredmeny:
            if x in self.valasztott:
                szam+=1
        return szam
    @property
    def eredmeny(self):
        return self.__eredmeny
    @property
    def valasztott(self):
        return self.__valasztott
    def addvalasztott(self,szam):
        self.valasztott.add(szam)
    def removevalasztott(self,szam):
        self.valasztott.discard(szam)




class OtosLotto(Lotto):
    def __init__(self,alapnyeremeny):
        Lotto.__init__(self,5,90,5)
    #     Az ötös lottó: 5 számmal játszasz.90-ből kihúznak 5 öt,és ha eltaláltad mind az 5 öt akkor jackpot
    def __str__(self):
        str="Ötös lottó"
        return str













#main
x=OtosLotto(1)
print(x.lottohuzas())
x.addvalasztott(22)
print(x.hanyjo())
#
