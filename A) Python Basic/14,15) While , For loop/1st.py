# While loop
i = 1
while i < 6:
  print("Output1 is ",i)
  i += 1
# break
i = 1
while i < 6:
  print("output2 is",i)
  if i == 3:
    break
  i += 1
# Continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print("output3 is",i)
  
#Else 
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
#For loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#break
for i in range(9):
  if i > 3:
    break
  print(i)

#Continue
for i in range(9):
  if i == 3:
    continue
  print(i)
