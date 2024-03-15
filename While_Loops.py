#In this code we are showing how a while loop work in python
#Here I am going to prompt a user for students names ages and display the
#The program will loop as many times as it can unless the user enters a top

print("Enter student name: ")
name = input()
print(" ")

print("Enter student surname: ")
surname = input()

print(" ")

print("Enter student age: ")
age = int(input())

sentinel = ''

while True:

    if name == sentinel:
        break
    
    print("Enter student name: ")
    name = input()
    print(" ")

    print("Enter student surname: ")
    surname = input()

    print(" ")

    print("Enter student age: ")
    age = int(input())

    

    

print(f"{name}  {surname} is {age} year(s) old.")