# instance methods
# are fn defined inside a class abd can only call on an instance of that class.
class Human:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

simon = Human("Simon" , 20)
print(simon.description())
print(simon.speak("Hello!"))


# How to inherit from another class
# inheritance = is where one class takes attributes and methods of another class
# child class inherits  from a parent class.
# child class takes attributes and methods from the parent class.

class Parent:
    hair_color = "brown"
    pass

class Child(Parent):
    pass

# overriding
class Parent:
    hair_color = "brown"
    pass

class Child(Parent):
    hair_color ="black"
    pass