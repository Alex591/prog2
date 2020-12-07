import random


class Lotto():
    def __init__(self,jelolesek,osszesszam,mennyithuzni):
        # Jelolesek:Mennyit kell kijelolni
        # osszesszam:Milyen intervallumból kell azokat kijelölni
        # mennyithuzni: Mennyi számot kell kihúzni
        self.jelolesek = jelolesek
        self.osszesszam = osszesszam
        self.mennyithuzni = mennyithuzni
        # Valasztott:A felhasználó által választott,vagy a gép által generált számsorozat
        # Eredmény: A lottóhúzás végeredménye
        self.__valasztott = set([])
        self.__eredmeny = set([])

    # itt történik maga a lottóhúzás

    def lottohuzas(self):
        # A while szerepe az,hogy ha netalán a randomszámgenerátor kétszer adná ugyanazt a számot,ne legyen kevesebb szám.
        # vagyis garantálja hogy a kellő számú szám lesz kihúzva
        while len(self.eredmeny) < self.jelolesek:
            self.eredmeny.add(random.randint(1, self.osszesszam))
        return self.eredmeny

    # Számot ad vissza,attól függően hány számot talált el Hősünk

    def hanyjo(self):
        szam = 0
        for x in self.eredmeny:
            if x in self.valasztott:
                szam += 1
        return szam

    # True vagy False értéket ad vissza,ha True akkor a kellő számú szám van bejelölve

    def isvalid(self):
        if len(self.valasztott) == self.mennyithuzni:
            return True
        return False

    # setterek,getterek
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
        # A nyereményre félretett összeg
        self.__prizepool = prizepool
        # A súly százalékban értetendő,pl a telitalálatos a nyereményre félretett pénzösszeg 81.2%-át kapja.
        self.suly = [0, 0.12, 0.015, 0.158, 0.16, 0.5]

    #     Az ötös lottó: 5 számmal játszasz.90-ből kihúznak 5 öt,és ha eltaláltad mind az 5 öt akkor jackpot
    def __str__(self):
        str = "Ötös lottó"
        return str

    # Egy fájlból olvassa be a nyereményt. Ha Hősünk esetleg okos akarna lenni,és mondjuk megpróbálja nyereménynek berakni az ú betűt,akkor nem engedjük neki.
    def readprizepool(self):
        try:
            fajl = open("nyeremeny.txt", 'r')
            for x in fajl:
                self.setprizepool(x)
        except:
            pass

    # Számot ad vissza,a nyeremény értékét
    def penznyereseg(self):
        x = self.hanyjo()
        y = self.suly[x] * self.prizepool
        return y

    # getterek,setterek
    @property
    def prizepool(self):
        return self.__prizepool

    def setprizepool(self, p):
        # itt csekkoljuk hogy szám e
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
