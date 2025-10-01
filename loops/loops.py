#loops
    # for loops
# while loops

# for loops = run  some condition a set number of times
#            = loops over iterable objects

#syntax
#for (variable) in (iterable):
#    do sth with variable (/iterable)(/variable)


#for i in range (5):
#    print ("hello")

#for letter in " python":
#   print(letter)

#   iterable  = is an object that returns its members one at a time



#for loops and lists

#alist = [1,2,3,"a","b","hello"] # we created a list
#for item in alist:
#   print(item)

#print (alist[2]) # we can scces individual elements of a list
#print (alist[1] + alist[2]) 

# while loops
# syntax

# while <expression evaluates="" to="" true="">:
#    do something</expression>

x = 1
while x <=5:
    print(x)
    x += 1  #we print x and increase it by 1. it keeps happening as long as x <= 5
# as long as expression evaluates to true, block inside while loop executes repeatedly

i = 1
while i <= 4:
    print(i)
    i = i + 1