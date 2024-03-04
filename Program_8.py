#Filter prime numbers from a list
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

def checkPrime(num):
    Flag=True
    for i in range(2,num//2):
        if num%i==0:
            Flag=False
    return Flag

def filterList():
    print("-- Filter Prime numbers from List of numbers --")
    list1 = list_input()
    list2 = []
    for i in list1:
        check = checkPrime(i)
        if check==True:
            list2.append(i)
    print("Original List : ",list1)
    print("Filtered list : ",list2)

filterList()
