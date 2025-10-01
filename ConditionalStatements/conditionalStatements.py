#COnditional Statements 
 #   if else
  #  ty/except
   # switch

day = "Sunday"
if day == "Monday":
    weekday = "day 1 "
elif day == "Tuesday":
    weekday = "day 2 "
elif day == "Wednesday":
    weekday = "day 3 "
elif day == "Thursday":
    weekday = "day 4 "
elif day == "Friday":
    weekday = "day 5 "
else :
    weekday =" weekend"

# conditional expressions /ternary operator
age = 18
is_adult = "yes" if age < 18 else "not an adult"

# value_if_true if condition else value_if_false


# Try/Except statements
def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")