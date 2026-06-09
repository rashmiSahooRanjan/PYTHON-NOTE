#1. is (Returns True if both variables are the same object)
x=["apple", "banana"]
y=["apple", "banana"]
print(x is y) 

# The answer is False because x and y are two different objects in memory.
# It check the memory address of both variables and since they are different, it returns False.


#2. is not (Returns True if both variables are not the same object)
print(x is not y)
# The answer is True because x and y are two different objects in memory.
# It check the memory address of both variables and since they are different, it returns True.

print(x == y)
# The answer is True because it checks if the values of both variables are equal.