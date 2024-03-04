#Read and print a file
def readFile():
    filename=input("Enter the filename : ")
    try:
        file = open(filename,"r")
        for i in filename:
            print(i)
        file.close()
    except FileNotFoundError:
        print("Error : File not found!")

readFile()
