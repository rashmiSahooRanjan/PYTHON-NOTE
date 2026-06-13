class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Rashmi")
print(s1.name)


# Accessing Properties with self 
class Student:
       def __init__(self, name):
              self.name = name
       def show_name(self):
               print(self.name)
s1 = Student("Rashmi")
s1.show_name()

#Calling Methods with self 
class Student:
    def greet(self):
        print("Hello")
    def welcome(self):
        self.greet() # calling another method
s1 = Student()
s1.welcome()
