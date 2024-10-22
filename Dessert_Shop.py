class DessertItem:
    def __init__(self,name):
        self.name = name

        def name():
            pass

class Candy(DessertItem):
    def __init__(self, name, candy_weight, price_per_pound):
        self.name = name
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

        def candy_weight():
            pass

        def price_per_pound():
            pass

class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity, price_per_dozen):
        self.name = name
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

        def quantity():
            pass

class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        self.name = name
        self.scoop_count = scoop_count
        self. price_per_scoop = price_per_scoop

        def scoop_count():
            pass
        
        def price_per_scoop():
            pass

class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        self.name = name
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.topping_name = topping_name
        self.topping_price = topping_price
        super().__init__(name, scoop_count, price_per_scoop, topping_name, topping_price)

        def topping_name():
            pass

        def topping_price():
            pass