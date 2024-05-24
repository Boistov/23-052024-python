class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)
    def bark(self):
        print(f"{self.name} says Woof!")
    def print_info(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}, Tricks: {', '.join(self.tricks)}")

print(my_dog := Dog("buddy", "golden retriever", 3))
print(my_dog.add_trick("roll Over"))
print(my_dog.add_trick("fetch"))
print(my_dog.bark())
print(my_dog.print_info())