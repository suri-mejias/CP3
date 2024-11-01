class Monster:
    def __init__(self,name,birthplace):
        self.name = name
        self.birthplace = birthplace

    def attack_method(self):
        print(self.name, " from ", self.birthplace, " attacks! " )

class Vampire(Monster):
    def attack_method(self):
        print(self.name, "ATTEMPTS TO BITE OPPONENT! ")

class Zombie(Monster):
    def attack_method(self):
        print(self.name, "ATTEMPTS TO GET CLOSE TO OPPONENT AND BITE HEAD OFF!! ")

class Dragon(Monster):
    def attack_method(self):
        print(self.name, "ATTEMPTS TO BREATH FIRE ON OPPONENT! ")

class Megalodon(Monster):
    def attack_method(self):
        print(self.name, "ATTEMPTS TO DRAG  OPPONENT INTO OCEAN!!!")

vampire = Vampire("DRACULA", "Transylvania")
zombie = Zombie("JERRY","Jerry's Cave")
dragon = Dragon("LARRY", "Larry's Cave")
megalodon = Megalodon("HARRY", "Harry's Cave")

vampire.attack_method()
dragon.attack_method()
zombie.attack_method()
megalodon.attack_method()
