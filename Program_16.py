#Count Uppercase Characters in a file
def countUpperCase():
    filename = input("Enter the filename : ")
    file = open(filename,"r")
    upper_count=0
    characters = []
    text = file.read()
    characters = list(text)
    for i in characters:
        if i.isupper()==True:
            upper_count+=1
    print("Total number of UpperCase letters in the file : ",upper_count)
    file.close()

ch='y'
while(ch=='y' or ch=='Y'):
    try:
        countUpperCase()
    except FileNotFoundError:
        print("Sorry, File not found!")
        continue
    ch = input("Do you wish to go again?(Y/N) : ")

