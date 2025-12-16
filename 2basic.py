#String Methods in Python
#touppercase
a = "Hello, World!"
print(a.upper())
#tolowercase
print(a.lower())
#slipting the string
print(a.split(","))
#replace
print(a.replace("World", "There"))
#check if string starts with
print(a.startswith("Hello"))
#check if string ends with
print(a.endswith("!"))
#find a substring
print(a.find("World"))
#length of the string
print(len(a))
#strip whitespace
b = "   Hello, World!   "
print(b.strip())
#concatenate strings
c = "Hello"
d = "World"
print(c + " " + d)
#formatting strings
name = "Vignesh"
age = 25
print("My name is {} and I am {} years old.".format(name, age))