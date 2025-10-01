# class = blueprint for making objects
# instance (__init__) = object created from a class 
            # eg my_car = Car("red") → this is one instance.
            #  is an object thats built form a class and contains real data

# object = another word for instance 
# oop = focuses on objects ( things with data + actions/behaviors)
# fn = reusable block of code 
# method = fn inside a class that belongs to an object 
        # eg class Dog:
#               def bark(self):
#                   print("Woof!")


# attribute = variable inside/within an object
# eg my_car.color = "red"

# property = attribute conrolled by methods 
#  Dunder methods
    #__init__(self):    

# defining a class
# classes define fn(methods) which identify behaviors and actions that an object created from tha class can perform with its data

class Dog:
    pass

class Car:
    def __init__(self, name , color): # instance attribute
        self.name = name # creates an attribute called name and assigns value of the name parameter to it 
        self.color = color # creates an attribute called color and assigns value of the color parameter to it


# class attribute = variable that belongs to the class itself, not just one object (instance).
#  attributes that have same value to all class instances . Defined outside of __init__()

#class Human:
#    species = "Homo sapiens" # class attribute =defined directly beneath class name

#   def __init__(self , name , age ):
#        self.name = name
#        self.age = age

#        pass

# how to instantiate a class
# instantiate = creating a new object from a class
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

# Dog() # instantiate
rex = Dog("Rex",5 ) # first dog instance
mdogo = Dog("Mdogo", 10) # 2nd dog instance
# after creating dog instances , acces their instance attributes 

print (rex.name)

rex.age =7

print (rex.age)
print (mdogo.name)
print (mdogo.age)

mdogo.species = 'Felis silvestris'

print (rex.species)
print (mdogo.species)


