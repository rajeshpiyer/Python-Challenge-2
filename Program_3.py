#Search for a string in a file
def readFile():
    filename=input("Enter the filename : ")
    try:
        file = open(filename,"r")
        return file
    except FileNotFoundError:
        print("Error : File not found!")

def search():
    file = readFile()
    string = input("Enter the String to search in the file : ")
    line_count=0
    for i in file:
        line_count+=1
        if string.lower() in i.lower():
            print("Yes, String found in Line ",line_count)
        else:
            print("String not found in the file!")
    file.close()

search()