#.Write a Python program input and add two integers only and handle the exceptions.

def sum():
    print("Sum of two integers")
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    print(f"SUM = {a+b}")

ch='y'
while(ch=='y' or ch=='Y'):
    try:
        sum()
    except ValueError:
        print("Numbers need to be Integers")
        continue
    ch = input("Do you wish to go again?(Y/N) : ")