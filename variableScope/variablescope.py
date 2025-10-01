##  Scope = area in code where specific variable can be called
##     =areas in code where certain data is available to you

name = "Simon"  # global variable
def greet():
    print(f"Hello , {name}")
greet()

# global variables can be accessible inside function

first_name = "Sai"
def greet2(first_name):
    print(f"Hello , {first_name}")
greet2("Joe")

# local variable = defined inside function and cant be accessed outside function
def greet3():
    last_name = "Smith"
    print(f"My last name is , {last_name}")