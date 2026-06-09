a=5;
b=10;

#1. and (Returns True if both statements are true)
if a>6 and b<10:
    print("True");
else:
    print("False");
    
#2. or (Returns True if one of the statements is true)
if a>6 or b<10:
    print("True")
else:
    print("False")
    
#3. not (Reverse the result, returns False if the result is true)
if not(a>6 and b<10):   
    print("True")
else:
    print("False")