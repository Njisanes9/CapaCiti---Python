#In this code we are showing how if else statements work in python
#Here I am going to show how a program makes decision based on the age of user entry

print("Enter your name: ")
name = input()
print(" ")


print("Enter your age: ")
age = int(input())

def UserInput():
    if(age < 13):
        print("Good day " + name + " you are young.")
    else:
        if(age > 13 and age < 20):
            print("Good day " + name + " you are a teenager.")
        else:
            print("Good day " + name + " you are a old.")

UserInput()



