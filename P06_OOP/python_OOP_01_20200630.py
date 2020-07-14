#Izveidojam objektu
class Cilveks:
    Vards = ""
    Uzvards = ""
    Vecums = int(0)

    def PilnsVards(self):
        print "Pilns vards ir", self.Vards, self.Uzvards

    def DzimsanasDiena(self):
        self.Vecums = self.Vecums + 1
        print "Sodien", self.Vards, self.Uzvards,"palika", self.Vecums,"gadu"

#Komandas testeeshanai
a = Cilveks()
a.DzimsanasDiena()
a.DzimsanasDiena()
a.DzimsanasDiena()
a.PilnsVards()
a.Vards = "Emils"
a.Uzvards = "Vizulis"
a.PilnsVards()
a.DzimsanasDiena()
a.Vecums = 19
a.DzimsanasDiena()

#Radniecibas izmeginasana
class Students(Cilveks):
    MacibuIestade = ""

    def Skola(self):
        if self.MacibuIestade=="":
            self.MacibuIestade=input("Ievadiet maaciibu iestaades nosaukumu:")
        else:
            if self.Vards=="" or self.Uzvards=="":
                if self.Vards=="": self.Vards = input("Ievadiet vaardu:")
                if self.Uzvards=="": self.Uzvards = input("Ievadiet uzvaardu:")
            print self.Vards, self.Uzvards, "maacas", self.MacibuIestade

#Radniecibas testeeshana
b = Students()
b.Vards = "Ano"
b.Uzvards = "niims"
b.MacibuIestade = "RTU"
b.PilnsVards()
b.Skola()
