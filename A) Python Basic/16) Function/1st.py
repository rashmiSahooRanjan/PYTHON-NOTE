def my_function():   #Creating a function
  print("Hello from a function") 
my_function()    #Call this function, To call a function, write its name followed by parentheses

#Return value
def get_greeting():
  return "Hello from a function"
message = get_greeting()
print(message)

#Pass Statement
x = 10
if x > 5:
    pass

#Function Arrguments 
def my_function(fname):
  print(fname + " Referenes")
my_function("Email")
my_function("Phone")
my_function("Linus")