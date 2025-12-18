set1 = {56, 23, 45, 67, 89}
print(set1)
list1 = [23, 45, 67, 89, 12, 34]
print(list1)
dict1 = {"name": "Vignesh", "age": 25, "city": "Chennai", "country": "India", "occupation": "Developer"}
print(dict1)
#only keys
print(dict1.keys())
#only values
print(dict1.values())
#frozenset
frozenset1 = frozenset({23, 45, 67, 89, 12, 34})
print(frozenset1)
#iterating frozenset
for item in frozenset1:
    print(item)
#while loop
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

#functions
def greet(name):
    return "Hello, " + name + "!"
print(greet("Vignesh"))

#if a user enters the year we need to find the age
year = int(input("Enter year: "))
current_year = 2024
age = current_year - year
print("Your age is", age)

#request libreary
import requests
response = requests.get("https://api.github.com")
print(response.text)