#Filter numbers which are divisible by 3 or 5 from a list
import math

def list_input():
    list1 = []
    ch = 'y'
    while ch.lower() == 'y':
        item = input("Enter the item: ")
        while not item.isdigit():
            item = input("Invalid Item!\nEnter the item: ")
        list1.append(int(item))
        ch = input("Add another item? (y/n): ")
    return list1

def checkIfDivisible(num):
    Flag=False
    if num%3==0 or num%5==0:
        Flag=True
    return Flag

def filterList():
    print("-- Filter numbers divisible by 3 or 5 from List of numbers --")
    list1 = list_input()
    list2 = []
    for i in list1:
        check = checkIfDivisible(i)
        if check==True:
            list2.append(i)
    print("Original List : ",list1)
    print("Filtered list : ",list2)

filterList()