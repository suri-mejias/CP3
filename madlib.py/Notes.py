# Started class with keyboard class and then named it using Pascal Case
class Animal:
    #Start with the constructor (defines all th attributes of the object created)
    def __init__(self, name, species, age, gender, rarity):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.rarity = rarity

    #Methods are functions inside of the class
    def fight(self,other):
        if len(self.name) > len(other.name):
            other.losses += 1
            return self.name
        elif len(self.name) < len(other.name):
            self.losses += 1
            return other.name
        else:
            self.losses += 1
            return "tie"
    
    #Makes a more readeable string when printed
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nSpecies: {self.species}\nGender: {self.gender}\nRarity: {self.rarity}\n"
#We generally store objects in variables (individualy or in a list) so we can use it 
cat = Animal("Tom", "Cat", 21, "Male", "Common")
frog = Animal("Jarrod", "Poison Dart Frog", 500, "Female", "Rare")

# To call methods you put the name of the object.name of the method(any arguments that are needed)
cat.losses = 0
frog.losses = 0
print(cat.fight(frog))

cat.name = "Thomas"
print(cat.losses)

print(cat.fight(frog))
print(cat.losses)
print(frog.losses)

cat = None
print(cat)





