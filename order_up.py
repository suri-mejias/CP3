class OrderUp:
    def __init__(self, menu):
        self.drink = None
        self.appetizer = None
        self.entree = None
        self.side = [None, None]
        self.dessert = None
        self.menu = menu
        self.total = 0

    def place_order(self):
        print("\nWelcome to Suri's restaurant! Let's place your order.")
        self.drink = self.ask_for_item("drink")
        self.appetizer = self.ask_for_item("appetizer")
        self.entree = self.ask_for_item("entree")
        self.side[0] = self.ask_for_item("side") 
        self.side[1] = self.ask_for_item("side") 
        self.dessert = self.ask_for_item("dessert")

    def ask_for_item(self, category):
        print(f"\nWould you like to order a {category}? Here are the available options:")
           
        item = input(f"Please enter the {category} you would like, or press Enter to skip: ").title()

        if item and self.check_if_on_menu(item, category):
            self.total += self.menu[category][item]
            return item
        elif item:
            print(f"Sorry, we don't have {item} in the {category} category.")
        return None

    def check_if_on_menu(self, item , category):
        if item in self.menu.get(category, {}):
            return True
        return False

    def print_order(self):
        print("\nHere is your order: ")
        if self.drink: 
            print(f"Drink: {self.drink}")
        if self.appetizer:
            print(f"Appetizer: {self.appetizer}")
        if self.entree:
            print(f"Entree : {self.entree}")
        if self.side[0]:
            print(f"First Side: {self.side[0]}")
        if self.side[1]:
            print(f"Second Side: {self.side[1]}")
        if self.dessert:
            print(f"Dessert: {self.dessert}")
        if not any([self.drink, self.appetizer, self.entree, self.side[0], self.side[1], self.dessert]):
            print("No items ordered.")
        else:
            print(f"\nTotal: ${self.total:.2f}")

    def change_item(self, category):
        current_item = getattr(self, category)
        if current_item:
            print(f"\nYour current {category} is: {current_item}")
        new_item = self.ask_for_item(category)
        setattr(self, category, new_item)

menu = {
    "Drink": {"Coke": 2.0, "Water": 0.0, "Malta": 3.0},
    "Appetizer": {"Fries": 3.0, "Salad": 4.0, "Bread Rolls": 5.0},
    "Entree": {"Burger": 8.0, "Pizza": 10.0, "Steak": 15.0},
    "Sides": {"Mac n Cheese": 3.0, "Mashed Potatoes": 3.5, "Salad": 4.0},
    "Dessert": {"Ice Cream": 3.0, "Flan": 3.5, "Cake": 2.0}
}

# Create an order 
order = OrderUp(menu)

# Place an order
order.place_order() 

# Print the order 
order.print_order() 

# Allows the user to change an item
change = input("\nWould you like to change an item in your order? (yes/no): ").lower()
if change == "yes":
    category_to_change = input("Which category would you like to change? (drink/appetizer/main course/sides/dessert): ").lower()
    order.change_item(category_to_change)

# Print the final order
order.print_order()