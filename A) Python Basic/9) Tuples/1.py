# Tuple is Ordered
a = ("red", "green", "blue")
print(a[0])
print(a[1])

# Tuple is Unchangeable
b= ("red", "green", "blue")
# b[0] = "yellow"  # This will raise an error
print(b[0])

#Tuple Allows Duplicate Values
c = ("red", "green", "blue", "red")
print(c)

# Tuple Length - len() function
d = ("red", "green", "blue")
print(len(d))

# Check the Type of a Tuple
e=("red")
print(type(e))  # This is a string, not a tuple

f = ("red",)
print(type(f)) # This is a tuple 

# Negative Indexing
g = ("apple", "banana", "cherry")
print(g[-1])

# Range of indexes
h = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(h[2:5])  # This will print items from index 2 to 4
#Leaving Start Value Empty
print(h[:4])   # This will print items from the beginning to index 3
#Leaving End Value Empty
print(h[2:])   # This will print items from index 2 to the end
# Negative Range Indexing
print(h[-4:-2])  # This will print items from index -4 to -2

# Check if Item Exists by the help of "in" keyword
i= ("apple", "banana", "cherry")
if "apple" in i:
    print("Yes")

# convert tuple to list
j = ("apple", "banana", "cherry")
k = list(j)
print(k)

# convert list to tuple
l = ["apple", "banana", "cherry"]
m = tuple(l)
print(m)

# Add items to a tuple :- by the append() method. Tuples cannot be changed directly, but you can convert it into a list, add the item, and convert it back to a tuple.
n = ("apple", "banana", "cherry")
o = list(n)
o.append("orange")
n = tuple(o)
print(n)

# Add tuple to a tuple :- by the + operator
p = ("apple", "banana", "cherry")
q = ("orange",)
r = p + q
print(r)

# Remove items from a tuple :- by the remove() method. Tuples cannot be removed directly, but you can convert it into a list, remove the item, and convert it back to a tuple.
s = ("apple", "banana", "cherry")
t = list(s)
t.remove("banana")
s = tuple(t)
print(s)

# Delete the tuple :- by the del keyword
u = ("apple", "banana", "cherry")
del u
print(u)  # This will raise an error because the tuple has been deleted

# count() Method:- The count() method counts how many times a value appears in the tuple. Syntax :- tuple.count(value)
fruits = ("apple", "banana", "cherry", "apple")
x = fruits.count("apple")
print(x)

# index() Method:- The index() method finds the position of a value in the tuple. Syntax:- tuple.index(value). 
fruits = ("apple", "banana", "cherry")
x = fruits.index("banana")
print(x)


