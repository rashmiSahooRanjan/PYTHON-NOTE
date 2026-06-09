# List
fruits = ["apple", "banana", "mango"]
print(fruits)
#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#create the new list by the help of list()
thislist=list(("apple", "banana", "cherry")) 
print(thislist)
#you can access the item using square bracket[].
thislist = ["apple", "banana", "cherry"]
print(thislist[1])	
# Negative Indexing:- Negative index means counting from the end.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#Range of Indexes:-
thislist = ["apple", "banana", "cherry", "orange", "kiwi"]
print(thislist[1:4])
#Leave Start Empty
thislist = ["apple", "banana", "cherry", "orange", "kiwi"]
print(thislist[:3])
#Leave end Empty
thislist = ["apple", "banana", "cherry", "orange", "kiwi"]
print(thislist[1:])
#Negative Range
thislist = ["apple", "banana", "cherry", "orange", "kiwi"]
print(thislist[-4:-1])
#Check if Item Exists by the help of in keyword
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes")
#Change Item Value:- A list item can be changed using its index number.
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change Multiple Values (Range)
thislist = ["apple", "banana", "cherry", "orange"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Replace One Item with Two Items
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Replace Two Items with One Item
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append:- Add item at the END
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend() → Add MANY items in the list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove() → Remove the specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#popup() → Remove the specified index, (or the last item if index is not specified)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#popup without indexno
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Delete the list completely
thislist = ["apple", "banana", "cherry"]    
del thislist
print(thislist) #this will raise an error because the list no longer exists

#clear() → Empties the list, but list still exists
thislist = ["apple", "banana", "cherry"]
thislist.clear()