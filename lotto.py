import random

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
        self.valasztott=set([])
        self.eredmeny = set([])

    def lottohuzas(self):

        while len(self.eredmeny)<self.jelolesek:
            self.eredmeny.add(random.randint(1,self.osszesszam))
        return self.eredmeny
    def inputszamok(self,gepi):
        # A gép generálja le a számokat
        if gepi:
            while len(self.valasztott)<self.jelolesek:
                self.valasztott.add(random.randint(1,self.osszesszam))
            return self.valasztott
        # Hősünk pityegi be a számokat
        else:
            while len(self.valasztott) < self.jelolesek:
                szam=""
                # itt kell egy kis kivételkezelés mert Hősünk néha becsiccsent és szerelmei nevét akarja megtenni lottón
                valid=False
                while not valid:
                    while not szam.isnumeric():
                        szam=input("Adj egy számot")








    def hanyjo(self):
        szam=0
        for x in self.eredmeny:
            if x in self.valasztott:
                szam+=1
        return szam


class OtosLotto(Lotto):
    def __init__(self,alapnyeremeny):
        Lotto.__init__(self,5,90,5)
    #     Az ötös lottó: 5 számmal játszasz.90-ből kihúznak 5 öt,és ha eltaláltad mind az 5 öt akkor jackpot
    def __str__(self):
        str="Ötös lottó"
        return str













#main
x=OtosLotto(1)
# print(x.lottohuzas())
print(x.inputszamok(False))
# print(x.hanyjo())

