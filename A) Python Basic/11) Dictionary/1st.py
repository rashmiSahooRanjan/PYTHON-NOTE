a= {"name": "Rashmi", "age": 22,"course": "Python"}
print(a)

#Access Item :- by the square bracket
b={"name": "Rashmi", "age": 22,"course": "Python"}
print(b["name"])

#Access Item:- by the help of get method
c = { "name": "Rashmi", "age": 22}
print(c.get("age"))

#Change Item in Dictionary
d = {"name": "Rashmi","age": 22}
d["age"] = 23
print(d)

#Update the multipule values by :- update()
e= {"name": "Rashmi","age": 22}
e. update({"age": 24, "course": "AI"})
print(e)

#Add items in dictionary
f= {"name": "Rashmi"}
f["age"]=22
print(f)

#Remove item by the help of pop()
g= {"name": "Rashmi","age": 22}
g.pop("age")
print(g)

#popitem():-remove the last  vale
h= {"name": "Rashmi","age": 22}
h.pop("age")
print(h)

#Delete from specific key by del
i={ "name": "Rashmi","age": 22}
del i["age"]
print(i)

#delete the entire dictionary by del
# j={ "name": "Rashmi","age": 22}
# del j
# print(j)

