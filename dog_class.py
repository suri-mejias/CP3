class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def __str__(self):
        return f"{self.name} is a {self.breed}"

dogs = [
    Dog("Marceline", "German Sheperd"),
    Dog("Cajun", "Belgian Malinois")
    Dog("Daisy", "Border Collie")
    Dog("Rocky", "Golden Retriever")
    Dog("Bella", "Irish Setter")
    ]

for dog in dogs:
    print(dog)