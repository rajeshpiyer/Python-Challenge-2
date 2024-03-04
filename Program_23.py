#The program takes input from the user and checks if whether the input value is an integer or not, if the input 
#value is not an integer then the program will through a Type exception.

def takeInput():
    print("Check Input")
    a = int(input("Enter the number : "))
    return a

ch='y'
while(ch=='y' or ch=='Y'):
    try:
        a = takeInput()
        print("The number is : ",a)
    except ValueError:
        print("Number needs to be Integer")
        continue
    ch = input("Do you wish to go again?(Y/N) : ")