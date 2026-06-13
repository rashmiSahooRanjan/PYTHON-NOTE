class Student:
       def __init__(self, name):
              self.name = name
s1 = Student("Rashmi")
print(s1.name)


# Default Values in __init__() :- You can also set default values for parameters in  the __init__() method. 
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age
p1 = Person("Emil")
p2 = Person("Tobias", 25)
print(p1.name, p1.age)
print(p2.name, p2.age)

# Multiple Parameters:- The __init__() method can have as many parameters as you need. 

class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country
p1 = Person("Linus", 30, "Oslo", "Norway")
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
