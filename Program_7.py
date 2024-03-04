#Second Largest in a List
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

def largest(list1):
    largest_item=list1[0]
    for i in range(1,(len(list1)-1)):
        if list1[i]>largest_item:
            largest_item=list1[i]
    return largest_item

list1 = list_input()
largest_item = largest(list1)
list1.remove(largest_item)
largest_item = largest(list1)
print("The second largest item is : ",largest_item)