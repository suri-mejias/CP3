class Tech:
    def __init__(self,name,storage):
        self.name = name
        self.storage = storage

class Phone(Tech):
    def __init__(self,name,color,storage):
        self.name = name
        self.color = color
        self.storage = storage

    def __str__(self):
        return f"A {self.color} {self.name} with {self.storage} of storage"
    
    def __repr__(self):
        return f"Phone({self.name}, {self.storage}, {self.color})"

class Laptop(Tech):
    def __init__(self,size,name,storage):
        self.size = size
        self.name = name
        self.storage = storage

    def __str__(self):
        return f"{self.size}-inch {self.name} with {self.storage} of storage."
    
    def __repr__(self):
        return f"Laptop({self.name}, {self.storage}, {self.size})"
