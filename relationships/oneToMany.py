# one to many = relationship btwn two or more objects where one object is related to many objects.
# eg , a parent can have many children. but a child only has one parent.

# association = relationship btwn two objects but not in a way that one object owns another
# eg, a teacher can be associated with many students, but a student can have many teachers.

# aggregation = relationship btwn two objects where one object can exist without the other object.
# eg, a university can have many departments, but a department can exist without a university.



class ShopItem:
    def __init__(self , name, price):
        self.name = name
        self.price = price 
    

class   Buyer: # buyer class has shop_items attribute which is a list of ShopItem objects
    def __init__(self, name):
        
        self.name = name
        self.shop_items = []
# creating buyer and shop items
buyer = Buyer("John")
item1 = ShopItem("Laptop", 1000)
item2 = ShopItem("Phone", 500)

#adding shop items to buyer shop list
buyer.shop_items.append(item1)
buyer.shop_items.append(item2)

#print buyer's shop list
for item in buyer.shop_items:
    print(f"{buyer.name} bought {item.name} for ${item.price}")


# two one to many relationships
# setters and getters
# @ property decorator = allows us to define methods in a class that can be accessed like attributes


class Student:
    all= []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._teacher = None # teacher is a protected attribute
        Student.all.append(self)

    @property
    def teacher(self):
        return self._teacher 
    

    @teacher.setter
    def teacher(self, value):
        if not isinstance (value, Teacher ):
            raise ValueError("teacher must be an instance of Teacher class")
        self._teacher = value

class Teacher:
    def __init__(self, name):
        self.name = name

    @property
    def students(self):
        return [student for student in Student.all if student.teacher == self]
    
    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError("student must be an instance of Student class")
        student.teacher = self