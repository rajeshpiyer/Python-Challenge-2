def readFile(file_number):
    filename=input(f"Enter the name of file {file_number} : ")
    try:
        file = open(filename,"r")
        return file
    except FileNotFoundError:
        print("Error : File not found!")

def mergeFile():
    merged_file = open("MergedFile.txt","w")
    file_count=int(input("How many files do you want to merge? : "))
    file_number=1
    for i in range(1,file_count+1):
        file = readFile(file_number)
        for i in file:
            merged_file.write(i)
        file.close()
        file_number+=1
        merged_file.write("\n")
    print(f"{file_count} files successfully merged to MergedFile.txt !!!")

mergeFile()
