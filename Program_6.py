def list_input():
    list_string=[]
    ch='y'
    while(ch=='y' or ch=='Y'):
        string = input("Enter the String to add to list : ")
        list_string.append(string)
        print(list_string)
        ch=input("Do you wish to add another string to list? (Y/N) : ")
    return list_string

def sortList():
    list_string = list_input()
    print("Original List:\n", list_string)
    sorted_list = sorted(list_string, key=len, reverse=True)
    print("The sorted list is:\n", sorted_list)

sortList()