import datetime
a = datetime.datetime.now()
print(a) # Output :- 2026-06-08 10:44:17.260622


# Get Specific Parts of the Date
b = datetime.datetime.now()
print(b.year) # Output :- 2026

#Get the Weekday Name
c = datetime.datetime.now()
print(c.strftime("%A")) # Output :- Monday

# Create Your Own Date
# Syntax :- datetime.datetime(year, month, day)
d = datetime.datetime(2020, 5, 17)
print(d) # Output :- 2020-05-17 00:00:00

# Get Month Name
e = datetime.datetime(2018, 6, 1)
print(e.strftime("%B")) # otput :- june


f = datetime.datetime.now()
print(f.strftime("%d/%m/%Y")) # Output :- 08/06/2026

