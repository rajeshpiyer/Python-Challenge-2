#Print file with delay
import time

def delayPrint():
    filename = input("Enter the filename : ")
    file = open(filename,"r")
    for i in file:
        print(i)
        time.sleep(2)
    file.close()

ch='y'
while(ch=='y' or ch=='Y'):
    try:
        delayPrint()
    except FileNotFoundError:
        print("Sorry, File not found!")
        continue
    ch = input("Do you wish to go again?(Y/N) : ")