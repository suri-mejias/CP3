#polymorphism functions or methods can do multiple things based on given inputs
"""""
import math
from abc import ABC, abstractmethod 
class Shape(ABC):
    def __init__(self, x):
        self.x = x
    @abstractmethod
    def area(self):
        return 0
    
class Square(Shape):
    def area(self):
        return self.x * self.x
    
class Circle(Shape):
    def area(self):
        return math.pi * self.x**2
    
class Rectangle(Shape):
    def __init__(self, x, y):
        super(). __init__(x)
        self.y = y
    
    def area(self):
        return self.x + self.y

sqr = Square(4)
cir = Circle(4)
rec = Rectangle(5, 3)
shape = Shape(6)
print(sqr.area())
print(cir.area())
print(rec.area())
print(shape.area())
"""
class Contacts:
  def __init__(self):
    self.view = 'quit'
    self.contact_list = []
    self.choice = None
    self.index = None

def display(self):
    while True:
      if self.view == 'list':
        self.show_list()
      elif self.view == 'info':
        self.show_info()
      elif self.view == 'add':
        print()
        self.add_contact()
      elif self.view == 'quit':
        print('\nClosing the contact list...\n')
        break
def show_list(self):
    pass

def show_info(self):
    pass

def add_contact(self):
    pass

contacts = Contacts()
contacts.display()

def __init__(self):
  self.view = 'list'

  def show_list(self):
    print()
  if len(self.contact_list) == 0:
    self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
  else:
    self.view = 'quit'
  self.handle_choice()

  def handle_choice(self):
    if self.choice == 'q':
        self.view = 'quit'
    elif self.choice == 'a' and self.view == 'list':
        self.view = 'add'

class Information:
  def __init__(self):
    self.first_name = input('Enter their first name: ')
    self.last_name = input('Enter their last name: ')
    self.personal_phone = input('Enter their personal phone number: ')
    self.personal_email = input('Enter their personal email address: ')
    self.work_phone = input('Enter their work phone number: ')
    self.work_email = input('Enter their work email address: ')
    self.title = input('Enter their work title: ')

def __add__(self, new_contact):
    self.contact_list.append(new_contact)
  
def add_contact(self):
  self + Information()
  self.view = 'list'




  contacts = Contacts()
contacts.display()
