#file handling
#file= open('requirements.txt', 'r')  
#print(file.read())
#file.close()


#write to a file
file = open('data.txt', 'w')  #write mode
file.write("Hello, this is a sample text file.\n")
file.close()

#closeing the file automatically using with keyword
with open('data.txt', 'a') as file:  #append mode
    file.write("This line is added using append mode.\n")

#read the csv file
file= open('predictions.csv', 'r')  
print(file.read())
file.close()

#============= Exceptions in Python =============
#try and except block
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")