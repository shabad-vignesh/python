#write a python program to get output 5,4,3,2,1 using slicing
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]    
print(reversed_numbers)

#5,3,1 as the output
result = reversed_numbers[::2]
print(result)

#print multiplication table for the given number
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
#using functions to print the multiplication table
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
number = int(input("Enter a number to print its multiplication table: "))
multiplication_table(number)