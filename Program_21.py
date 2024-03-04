#Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

def list_input():
    list1=[]
    ch='y'
    while(ch=='y' or ch=='Y'):
        item=input("Enter the item : ")
        while(not item.isdigit()):
            item=input("Invalid Item!\nEnter the item : ")
        list1.append(int(item))
        ch=input("Add another item?(y/n) : ")
    return list1

def printList():
    list1 = list_input()
    num = int(input("How many elements do you want to print? : "))
    try:
        for i in range(0,num):
            print(list1[i])
    except IndexError:
        print("Index Error : Not that many elements in list ")

printList()

