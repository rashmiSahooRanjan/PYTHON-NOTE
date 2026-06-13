# Create the class
class rashmi1: #create the class  that is rashmi
    x=1
print(rashmi1.x) #access the class variable x using the class name and print it

# create the objectof the class
class rashmi2:
    x=5
p1= rashmi2() # create the object of the class rashmi2 and assign it to p1
print(p1.x)

# how to delet the object:- 
class rashmi3:
    x=10
p2= rashmi3() # create the object of the class rashmi3 and
print(p2.x) # print the value of x using the object p2
del p2 # delete the object p2
# print(p2.x) # this will give an error because p2 has been deleted

#pass statement in class
class rashmi4:
    pass # this is a placeholder for the class body, it does nothing
print(rashmi4) # this will print the class rashmi4