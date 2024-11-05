"""""


class Tech:
    def __init__(self,name,storage):
        self.name = name
        self.storage = storage

class Phone(Tech):
    def __init__(self,color):
        self.color = color

    def __str__(self):
        print (f"A {self.color} {self.name} with {self.storage} of storage")

class Laptop(Tech):
    def __init__(self,size):
        self.size = size

    def __str__(self):
        print(f")

"""