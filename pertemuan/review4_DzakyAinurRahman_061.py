class Hero:
    def __init__(self, nama, health, attack):
        self.nama = nama
        self.health = health
        self.attack = attack

    def serang(self, target):
        print(f"{self.nama} menyerang {target.nama}")

class Mage(Hero):
    def __init__(self, nama, health, attack, mana= 100):
        super().__init__(nama, health, attack)
        self.mana = mana

    def serang(self, target):
        print(f"{self.nama} menyerang musuh dengan magis {target.nama}")

class Assassin(Hero):
    def __init__(self, nama, health, attack, mana):
        super().__init__(nama, health, attack)
        self.mana = mana

    def serang(self, target):
        print(f"{self.nama} menyerang musuh dengan diam-diam {target.nama}")

class Doublerole(Assassin, Mage):
    def __init__(self, nama, health, attack, mana, jarak):
        super().__init__(nama, health, attack, mana)
        self.jarak = jarak

    def serang(self, target):
        return super().serang(target)
    
class assasinenergy(Assassin):
    def __init__(self, nama, health, attack, mana, energy):
        super().__init__(nama, health, attack, mana)
        self.energy = energy

    def serang(self, target):
        print(f"{self.nama} menyerang {target.nama} menggunakan energy")

balmond = Hero("Balmond", 1000, 10)
eudora = Mage("Eudora", 500, 10)

balmond.serang(eudora)
eudora.serang(balmond)

fanny = assasinenergy("Fanny", 800, 15, 100, 50)    
fanny.serang(balmond)

karina = Doublerole("Karina", 700, 20, 80, 5)
karina.serang(eudora)