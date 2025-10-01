## Functions= block of code that performs sequence of actions when called
## Syntax
def my_fn(param):
    print ("  ")
    return param + 1

# arguements 

def greetings(name):
    print(f"Hello , {name}")
greetings("Simon")

#default arguements
def greet(name="Engineer"):
    print(f"Hello , {name}")
greet()
greet("Sai")

# return values
def stylish_painter():
    best_hairstyle = "Bob Ross"
    print(best_hairstyle)
    return "Jean-Michel Basquiat"
#    return best_hairstyle
#    print(best_hairstyle)

stylish_painter()