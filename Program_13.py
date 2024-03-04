# Implement a program that simulates a basic calculator, allowing users to 
# perform arithmetic operations (addition, subtraction, multiplication, 
# division) on two numbers.

#Arithmetic Operations
def sum(a,b):
    return a+b

def subtract(a,b):
    return a-b

def product(a,b):
    return a*b

def divide(a,b):
    while(b==0):
        b=int(input("!! DIVISION BY ZERO NOT POSSIBLE !!\nEnter a valid divisor : "))
    return a/b

def floorDivision(a,b):
    while(b==0):
        b=int(input("!! DIVISION BY ZERO NOT POSSIBLE !!\nEnter a valid divisor : "))
    return a//b

def modulus(a,b):
    while(b==0):
        b=int(input("!! DIVISION BY ZERO NOT POSSIBLE !!\nEnter a valid divisor : "))
    return a%b

def exponent(a,b):
    return a**b

def num_input():
    
    a=input("\n\n\t\t-- INPUT VALUES --\nEnter first number : ")
    while(not a.isdigit() or a==None or a==""):
        a=input("!! INVALID INPUT !!\nEnter first number : ")
  
    b=input("Enter second number : ")
    while(not b.isdigit() or b==None or b==""):
        b=input("!! INVALID INPUT !!\nEnter first number : ")
        
    return int(a),int(b)

def num_output(choice,a,b):
    print("\n\n\t\t-- RESULT --")
    if choice==1:
        print(f'{a} + {b} = {sum(a,b)}')
    elif choice==2:
        print(f'{a} - {b} = {subtract(a,b)}')
    elif choice==3:
        print(f'{a} * {b} = {product(a,b)}')
    elif choice==4:
        print(f'{a} / {b} = {divide(a,b)}')
    elif choice==5:
        print(f'{a} // {b} = {floorDivision(a,b)}')
    elif choice==6:
        print(f'{a} % {b} = {modulus(a,b)}')
    else:
        print(f'{a} raised to {b} is {exponent(a,b)}')


def choice():
    choice=input("\t\t-- ARITHMETIC OPERATIONS --\n\n1.SUM\t2.Difference\t3.Product\t4.Quotient\n5.Floor Division\t6.Modulus\t7.Exponentiation\nEnter Your Choice : ")
    while(not choice.isdigit() or int(choice)<1 or int(choice)>7):
        choice=input("!! INVALID INPUT !!\nEnter your Choice : ")
    a,b=num_input()
    num_output(int(choice),a,b)

ch='y'
while(ch=='y' or ch=='Y'):
    choice()
    ch=input("Wish to continue?(Y/N) : ")
    