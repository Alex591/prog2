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
        self.__valasztott=set([])
        self.__eredmeny = set([])

    def lottohuzas(self):

        while len(self.eredmeny)<self.jelolesek:
            self.eredmeny.add(random.randint(1, self.osszesszam))
        return self.eredmeny

    def hanyjo(self):
        szam = 0
        for x in self.eredmeny:
            if x in self.valasztott:
                szam += 1
        return szam

    def isvalid(self):
        if len(self.valasztott) == self.mennyithuzni:
            return True
        return False

    @property
    def eredmeny(self):
        return self.__eredmeny

    def seteredmeny(self, e):
        self.__eredmeny = e

    @property
    def valasztott(self):
        return self.__valasztott

    def addvalasztott(self, szam):
        self.valasztott.add(szam)
    def removevalasztott(self,szam):
        self.valasztott.discard(szam)


class OtosLotto(Lotto):
    def __init__(self, prizepool):
        Lotto.__init__(self, 5, 90, 5)
        self.__prizepool = prizepool

        self.suly = [0, 0.004, 0.014, 0.02, 0.05, 0.812]

    #     Az ötös lottó: 5 számmal játszasz.90-ből kihúznak 5 öt,és ha eltaláltad mind az 5 öt akkor jackpot
    def __str__(self):
        str = "Ötös lottó"
        return str

    def readprizepool(self):
        try:
            fajl = open("nyeremeny.txt", 'r')
            for x in fajl:
                self.setprizepool(x)
        except:
            pass

    def penznyereseg(self):
        x = self.hanyjo()
        y = self.suly[x] * self.prizepool
        return y

    @property
    def prizepool(self):
        return self.__prizepool

    def setprizepool(self, p):
        if str(p).isnumeric():
            self.__prizepool = p


class SkandinavLotto(Lotto):
    def __init__(self, prizepool):
        Lotto.__init__(self, 7, 35, 7)
        self.__prizepool = prizepool
        # ilyen a százalékos eloszlása a nyereményeknek
        self.suly = [0, 0.004, 0.014, 0.02, 0.05, 0.112, 0.3, 0.5]

    def readprizepool(self):
        try:
            fajl = open("nyeremeny.txt", 'r')
            for x in fajl:
                self.setprizepool(x)
        except:
            pass

    def penznyereseg(self):
        x = self.hanyjo()
        y = self.suly[x] * self.prizepool
        return y

    @property
    def prizepool(self):
        return self.__prizepool

    def setprizepool(self, p):
        if str(p).isnumeric():
            self.__prizepool = p

# main
# x=OtosLotto(1)
# x.readprizepool()
# print(x.prizepool)
# print(x.lottohuzas())
# x.addvalasztott(22)
# print(x.hanyjo())
# #
