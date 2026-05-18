class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        def move(self):
            print("Drive!")

class boat:
   def __init__(self, brand, model):
        self.brand = brand
        self.model = model

   def move(self):
            print("Sail!")

class plane:
   def __init__(self, brand, model):
        self.brand = brand
        self.model = model

   def move(self):
            print("Fly!")

car1 = car("Ford", "Mustang")
boat1 = boat("Ibiza", "Touring 20")
plane1 = plane("Boeing", "747")

for X in (car1, boat1, plane1):
    X.move()
