class DessertItem:
    def __init__(self, name: str = ""):
        self.name = name

class Candy(DessertItem):
    def __init__(self, name: str = "", candy_weight: float = 0.0, price_per_pound: float = 0.0):
        self.name = name
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        super().__init__(name)

class Cookie(DessertItem):
    def __init__(self, name: str =  "", cookie_quantity: int = 0, price_per_dozen: float = 0.0):
        self.name = name
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        super().__init__(name)

class IceCream(DessertItem):
    def __init__(self, name: str = "", scoop_count: int = 0, price_per_scoop:  float = 0.0):
        self.name = name
        self.scoop_count = scoop_count
        self. price_per_scoop = price_per_scoop
        super().__init__(name)

class Sundae(IceCream):
    def __init__(self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0, topping_name: str = "", topping_price: float = 0.0):
        self.name = name
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.topping_name = topping_name
        self.topping_price = topping_price
        super().__init__(name, scoop_count, price_per_scoop)

class Order():
    def main():
        Candy("Candy Corn", 1.5, .25)
        Candy("Gummy Bears", .25, .35)
        Cookie("Chocolate Chip", 6, 3.99)
        IceCream("Pistachio", 2, .79)
        Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
        Cookie("Oatmeal Raisin", 2, 3.45)