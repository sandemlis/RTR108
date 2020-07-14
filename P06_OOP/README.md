# Object oriented programming

Šajā nodarbībā tika izmēģināta objektu orientēta programmēšana, kurā mēs izveidojām paši savu objekta šablonu un no tā veidojām objektus kuriem piešķīrām vērtības.

## Objekta šablona izveidošana

Lai izveidotu objektu, virspirms in nepieciešams tā šablons, kuram mēs definējam šī objekta īpašības.

>class Cilveks:
>    Vards = ""
>    Uzvards = ""
>    Vecums = int(0)
>
>    def PilnsVards(self):
>        print "Pilns vards ir", self.Vards, self.Uzvards
>
>    def DzimsanasDiena(self):
>        self.Vecums = self.Vecums + 1
>        print "Sodien", self.Vards, self.Uzvards,"palika", self.Vecums,"gadu"

un lai no šī šablona izveidotu objektu, kādam mainīgajam jāpiešķir visas īpašības, kas pastāv šajā objektā.

> a = Cilveks()

## Objektu radniecība

Veidojot šablonus objektiem ir iespējams mantot īpašības no cita šablona.
Izsaucot, jau iepriekš izveidoto šablonu, jaunā šablona veidošanas laikā, tas manto visas izsauktā šablona īpašības, kā arī piešķirt jaunizveidotajam jaunās īpašības.

>class Students(Cilveks):
>    MacibuIestade = ""
>
>    def Skola(self):
>        if self.MacibuIestade=="":
>            self.MacibuIestade=input("Ievadiet maaciibu iestaades nosaukumu:")
>        else:
>            if self.Vards=="" or self.Uzvards=="":
>                if self.Vards=="": self.Vards = input("Ievadiet vaardu:")
>                if self.Uzvards=="": self.Uzvards = input("Ievadiet uzvaardu:")
>            print self.Vards, self.Uzvards, "maacas", self.MacibuIestade
