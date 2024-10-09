class pokemon:
    def __init__(self, name, hp, typ, level):
        self.name = name
        self.hp = hp
        self.type = typ
        self.level = level

    def combat(self, other):
        if self.level > other.level:
            return f"{self.name} won!"
        elif self.level < other.level:
            return f"{other.name} has defeated you!  "
        else:
            return f"{self.name} and {other.name} both lose. "

    def __str__(self):
        return(f"""
            Name: {self.name}
            Type: {self.type}
            Level: {self.level}
            HP: {self.hp}
""")
    
# @classmethod, used to keep method from changing objects instances.
    def level_up(self):
        self.level += 1
        self.hp *= int( 1.5)

    @classmethod
    def pikachu(self):
        return pokemon(input("Give me a name "), 50, "Electric", 1)
    
    #Static methods do not require self or class
    @staticmethod
    def hp_update(poke):
        return poke.hp - 5

eevee = pokemon("JayRod", 37, "Normal", 2)

pika = pokemon. pikachu()
pika.hp = pokemon.hp_update(pika)
print(pika)
