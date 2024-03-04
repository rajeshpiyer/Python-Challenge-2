#Filter Perfect Square from a list
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

def checkPerfectSquare(num):
    root = math.isqrt(num)
    if root*root==num:
        Flag=True
    else:
        Flag=False
    return Flag

def filterList():
    print("-- Filter Perfect Square numbers from List of numbers --")
    list1 = list_input()
    list2 = []
    for i in list1:
        check = checkPerfectSquare(i)
        if check==True:
            list2.append(i)
    print("Original List : ",list1)
    print("Filtered list : ",list2)

filterList()