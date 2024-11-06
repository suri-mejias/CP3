from tech import (
    Phone,
    Laptop,
)

MyPhone = Phone("Iphone", "White", "256")
print(MyPhone)
MyLaptop = Laptop(20, "Lenovo", "692")
print(MyLaptop)

print(repr(MyPhone))
print(repr(MyLaptop))