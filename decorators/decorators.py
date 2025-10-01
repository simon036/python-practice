# Decorators = syntax that allows adding functionality to an object without modifying its structure 

# inner functions = functions within a function
def hello (name):
    print ("Hello")

    def greet ():
        print ("greetings")
        
        return greet
    
# decorators
