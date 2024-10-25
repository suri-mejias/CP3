class OrderUp:
<<<<<<< HEAD
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
=======
    def __init__(self, menu): 
        self.drink = None 
        self.appetizer = None 
        self.main_course = None 
        self.sides = [None, None] 
        self.dessert = None 
        self.menu = menu 
        self.total = 0 

    def place_order(self): 
        print("\nWelcome to Suri's Restaurant!") 
        self.drink = self.ask_for_item("drink") 
        self.appetizer = self.ask_for_item("appetizer") 
        self.main_course = self.ask_for_item("main course") 
        self.sides[0] = self.ask_for_item("sides") 
        self.sides[1] = self.ask_for_item("sides") 
        self.dessert = self.ask_for_item("dessert") 

    def ask_for_item(self, category):
        print(f"\nWould you like to order a {category}? Here are the options:")
        for item, price in self.menu.get(category, {}).items(): 
            print(f"- {item}: ${price:.2f}")
        item = input(f"Please enter the {category} you would like, or press Enter if you dont want anything: ").strip().lower()
>>>>>>> 54847288b7326df7f2c278c7dac3217d5afd88ab

        if item and self.check_if_on_menu(item, category): 
            self.total += self.menu[category][item] 
            return item
        elif item:
            print(f"Sorry, we don't have {item} in the {category} category.")
        return None

<<<<<<< HEAD
    def check_if_on_menu(self, item , category):
        if item in self.menu.get(category, {}):
=======
    def check_if_on_menu(self, item, category):
        if item in self.menu.get(category, {}): 
>>>>>>> 54847288b7326df7f2c278c7dac3217d5afd88ab
            return True
        return False 

    def print_order(self):
        print("\nHere is your order: ")
        if self.drink: 
            print(f"Drink: {self.drink}")
        if self.appetizer:
<<<<<<< HEAD
            print(f"Appetizer: {self.appetizer}")
        if self.entree:
            print(f"Entree : {self.entree}")
        if self.side[0]:
            print(f"First Side: {self.side[0]}")
        if self.side[1]:
            print(f"Second Side: {self.side[1]}")
=======
            print(f"Appetizer: {self.appetizer}") 
        if self.main_course:
            print(f"Main Course: {self.main_course}")
        if self.sides[0]:
            print(f"First Side: {self.sides[0]}")
        if self.sides[1]: 
            print(f"Second Side: {self.sides[1]}")
>>>>>>> 54847288b7326df7f2c278c7dac3217d5afd88ab
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
        if new_item:
            if current_item:
                self.total-= self.menu[category][current_item] 
        setattr(self, category, new_item)
        self.total += self.menu[category][new_item]

menu = {
<<<<<<< HEAD
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
=======
    "drink": {"coke": 3.0, "water": 0.0, "wine": 9.0},
    "appetizer": {"fries": 6.0, "salad": 4.0, "bread Rolls": 5.0},
    "main course": {"burger": 15.0, "pizza": 18.0, "steak": 22.0},
    "sides": {"mashed potatoes": 4.0, "mac n cheese": 3.5, "salad": 3.0},
    "dessert": {"ice Cream": 3.0, "brownies": 4.0, "cake": 2.0}
}
order = OrderUp(menu)
order.place_order()
order.print_order()

# Allows the user to change an item
while True:
    change = input("\nWould you like to change an item in your order?(yes/no): ").lower()
    if change == "yes":
        category_to_change = input("Which category would you like to change? (drink/appetizer/main course/sides/dessert): ").lower()
        if category_to_change in ["drink", "appetizer", "main course", "sides", "dessert"]:
            order.change_item(category_to_change) 
            order.print_order()

        else:
            print("Thats not a category, choose again.")

    elif change == "no":
        print("Alright good choice!")
        break
    else:
        print("Please say yes or no.")


>>>>>>> 54847288b7326df7f2c278c7dac3217d5afd88ab

