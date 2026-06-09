a = {"apple", "banana", "cherry"}
print(a)

#Unordered:-
b = { "apple", "banana","cherry"} 
print(b)

# No duplicates values
c = {"apple", "banana", "cherry", "apple"}
print(c) #Duplicate value "apple" will be ignored

#unindexed
d = {"apple", "banana", "cherry"}
# print(d[0]) #This will raise an error because sets are unindexed

# Add items :- by the help of add() method we can add items to a set
e = {"apple", "banana", "cherry"}
e.add("orange")
print(e)

# Remove items :- by the help of remove() method we can remove items from a set
f = {"apple", "banana", "cherry"}
f.remove("banana")
print(f)

#True and 1 are Same in Set
g = {True, 1, 2, 3}
print(g) #True and 1 are considered the same in a set, so only one of them will be stored.

#False and 0 are Same in Set
h = {False, 0, 1, 2}
print(h) #False and 0 are considered the same in a set, so only one of them will be stored.

#Length of Set :- by the help of len() method we can find the length of a set
i = {"apple", "banana", "cherry"}
print(len(i)) #Output: 3

#Set Constructor :- we can create a set using the set() constructor
j = set(("apple", "banana", "cherry"))
print(j) #Output: {'apple', 'banana', 'cherry'}

#Access Items :- we cannot access items in a set by index, but we can loop through the set using a for loop
k= ["apple", "banana", "cherry"]
print(k[0]) #Output: apple

# Access Items using a for loop
l = {"apple", "banana", "cherry"}   
for item in l:
    print(item) #Output: apple, banana, cherry (order may vary)
    
#Check Item Exists by in() :- we can check if an item exists in a set using the in keyword
m = {"apple", "banana", "cherry"}
print("banana" in m) #Output: True
print("grape" in m) #Output: False

#Not in keyword
n = {"apple", "banana", "cherry"}
print("banana" not in n) #Output: False
print("grape" not in n) #Output: True

#update() Method in Set :- it is used to add the multiple items
o = {"apple", "banana", "cherry"}
p = {"grape", "orange"}
o.update(p)
print(o) #Output: {'apple', 'banana', 'cherry', 'grape', 'orange'}

#discard() Method in Set :- it is used to remove the specified item from the set
q = {"apple", "banana", "cherry"}
q.discard("banana")
print(q) #Output: {'apple', 'cherry'}

#clear() Method in Set :- it is used to remove all items from the set
r = {"apple", "banana", "cherry"}
r.clear()
print(r) #Output: set() (an empty set)

#del Keyword in Set :- it is used to delete the set completely
s = {"apple", "banana", "cherry"}
del s
# print(s) #This will raise an error because the set has been deleted

#Frozenset() Method in Set :- it is used to create an immutable set
t = frozenset({"apple", "banana", "cherry"})
print(t) #Output: frozenset({'apple', 'banana', 'cherry'})

#Frozenset methods :- frozenset has the same methods as a regular set, but it does not have methods that modify the set (like add() or remove())
u = frozenset({"apple", "banana", "cherry"})
#copy() Method in Set :- it is used to create a copy of the set
v=u.copy() #Output: frozenset({'apple', 'banana', 'cherry'})
print(v)
#difference() Method in Set :- it is used to return a set that contains the difference between two sets
w = frozenset({"apple", "banana", "cherry"})
x = frozenset({"banana", "grape"})
print(w.difference(x)) #Output: frozenset({'apple', 'cherry'})
#insection() Method in Set :- it is used to return a set that contains the intersection of two sets
y = frozenset({"apple", "banana", "cherry"})
z = frozenset({"banana", "grape"})
print(y.intersection(z)) #Output: frozenset({'banana'})

#isdisjoint() Method in Set :- it is used to return True if two sets have no items in common, otherwise it returns False
a1 = frozenset({"apple", "banana", "cherry"})
b1 = frozenset({"grape", "orange"})
print(a1.isdisjoint(b1)) #Output: True

#issubset() Method in Set :- it is used to return True if all items in the set are present in another set, otherwise it returns False
a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)

#issuperset() Method in Set :- it is used to return True if all items in another set are present in the set, otherwise it returns False
a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))
print(a >= b)
print(a > b)

#union() Method in Set :- it is used to return a set that contains all items from both sets, duplicates are excluded
a = frozenset({1, 2, 3})    
b = frozenset({3, 4, 5})
print(a.union(b)) #Output: frozenset({1, 2, 3, 4, 5})

#symmetric_difference() Method in Set :- it is used to return a set that contains the symmetric difference between two sets, which means it will contain only the items that are not present in both sets
a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.symmetric_difference(b)) #Output: frozenset({1, 2, 4, 5})

