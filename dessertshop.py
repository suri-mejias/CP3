from dessert import (
    Candy,
    Cookie,
    IceCream,
    Sundaeer
)

class Order():
    
    def __init__(self, order = []):
        self.order = order

    def __str__(self);
        for item in self.order:
            print(f'{item}')
        
    def add(self, item):
        self.order.append(item)

    
def main():
    order.add((Candy("Candy Corn", 1.5, .25)))
    order.add(Candy("Gummy Bears", .25, .35)
    Cookie("Chocolate Chip", 6, 3.99)
    IceCream("Pistachio", 2, .79)
    Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    Cookie("Oatmeal Raisin", 2, 3.45)