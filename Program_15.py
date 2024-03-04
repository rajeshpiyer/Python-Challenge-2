#Copy Odd lines from one file to another
def copy():
    filename1 = input("Enter the name of file 1 : ")
    file1 = open(filename1,"r")
    filename2 = input("Enter the name of file 2 : ")
    file2 = open(filename2,"a")
    line_counter=1
    for i in file1:
        if line_counter%2!=0:
            file2.write("\n"+i)
        line_counter+=1
    file1.close()
    file2.close()
    file2 = open(filename2,"r")
    print("-------------------------")
    print("Displaying Merged File")
    print("-------------------------")
    for i in file2:
        print(i)
    file2.close()

ch='y'
while(ch=='y' or ch=='Y'):
    try:
        copy()
    except FileNotFoundError:
        print("Sorry, File not found!")
    ch=input("Do you wish to go again?(Y?N) : ")


