age = 24
print("My age is %d years" % age)

major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))
print("PI is approximately %f" % (22 / 7))
print("PI is approximately %60.50f" % (22 / 7))

meal2 = "spam\neggs\nbeans"


first_name = "John"
last_name = "Cleese"
age = 78
 
print(first_name + last_name , age)

a = 45
b = 15
c = 3
 
print(a - b / c)

quantity = 10
price = 5.0
total = quantity * price
tax = total / 5
 
Total = total + tax
 
print(total)

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5]) # it uses the double :: and its select the 1st index in list of strings

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"

print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[:-1:5])