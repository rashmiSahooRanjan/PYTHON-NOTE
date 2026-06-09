#Binary Types: bytes, bytearray, memoryview
#bytes :- Bytes are used when Python needs to work with binary (machine-readable) data instead of normal human-readable text.
# bytes data can not be changed.
x=b"Hello World"  # here b is used for byte . without you run the print(type(x)) then type will come string.
print(x)
print(type(x))
#bytearray :- bytearray is similar to bytes, but it can be changed (modified) after creation.
y= bytearray(5)
print(y)
print(type(y)) 
#memoryview :-   memoryview is used to access binary data efficiently without copying it in memory.
z = memoryview(bytes(5))
print(z)
print(type(z)) 

#or
x = bytes("Hello World", "utf-8")
print(x)
print(type(x))
y = bytearray("Hello World", "utf-8")
print(y)
print(type(y))
z = memoryview(bytes("Hello World", "utf-8"))
print(z)
print(type(z))
