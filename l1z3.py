
class Human():
    def __init__(self, imie, nazwisko, plec, wiek, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.wiek = int(wiek)
        self.konwertujWzrost(int(wzrost))

    def daneOsobowe(self):
        print("Imie: " + self.imie)
        print("Nazwisko: " + self.nazwisko)

    def daneGenetyczne(self):
        print("Plec: " + self.plec)
        print("wzrost: " + str(self.wzrost))

    def wszystkieInformacje(self):
        print("Imie: " + self.imie)
        print("Nazwisko: " + self.nazwisko)
        print("Plec: " + self.plec)
        print("wzrost: " + str(self.wzrost))
        print("wiek: " + str(self.wiek))

    def rosnij(self, nowyWzrost):
        self.wzrost = nowyWzrost

    def slub(self, noweNazwisko):
        self.nazwisko = noweNazwisko
        print("Gratulacje Pani " + noweNazwisko + "!")

    def konwertujWzrost(self, wzrostWcm):
        wzrostWmm = wzrostWcm * 10
        self.wzrost = wzrostWmm

czlowiek = Human("Anita", "Wlodarczyk", "Mezczyzna", 21, 180)
czlowiek. daneOsobowe()
czlowiek.daneGenetyczne()
czlowiek.wszystkieInformacje()
czlowiek.rosnij(190)
czlowiek.daneGenetyczne()
czlowiek.slub("Ciesla")
czlowiek.daneOsobowe()

##############

class Cat():
    def __init__(self, imie, rokUrodzenia, rasa, waga):
        self.imie = imie
        self.rokUrodzenia = rokUrodzenia
        self.rasa = rasa
        self.konwertujWage(int(waga))

    def Wolaj(self):
        print("Chodz, tu: " + self.imie)

    def wiek(self):
        print("rok: " + str(self.rokUrodzenia))
        wiek = 2023 - self.rokUrodzenia
        print("ilosc lat: " + str(wiek))

    def daneKota(self):
        print("Imie: " + self.imie)
        print("Rok Urodzenia: " + str(self.rokUrodzenia))
        print("Rasa: " + self.rasa)
        print("Waga: " + str(self.waga))

    def noweImie(self, noweImie):
        self.imie = noweImie

    def zmienWage(self, nowaWaga):
        self.waga = nowaWaga
        kot.konwertujWage(self.waga)
        print("Kot zmienia wage, na: " + str(self.waga))

    def konwertujWage(self, wagaWg):
        wagaWkg = wagaWg / 1000
        self.waga = wagaWkg

kot = Cat("Andrzej", 2010, "Dachowiec", 16500)
kot.Wolaj()
kot.wiek()
kot.daneKota()
kot.noweImie("Andruch")
kot.Wolaj
kot.zmienWage(10200)