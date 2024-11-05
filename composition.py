#Type of class that exists in another class (class has a other class)

class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine



    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
class Engine:
    def __init__(self, configuration, displacement, horsepower, torque):
        self.configuration = configuration
        self.diplaceent = displacement
        self.horsepower = horsepower
        self.torque = torque 

    def ignite(self):
        print("Vroom, vroom! ")

myEngine = Engine("V8", 5.8, 326, 344)
myCar = Car("Mazda", "Mazda3", 2013, myEngine)

#To call a composit class you must acess where it is saved
print(myCar)
myCar.engine.ignite