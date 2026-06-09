#Set Types= set, frozenset
#set
x={"a","b","c"}
print(type(x))
#frozenset
y=frozenset({"p","q","r"})
print(type(y))

#orv
x=set("abc")
print(type(x))          
y=frozenset("pqr")
print(type(y))