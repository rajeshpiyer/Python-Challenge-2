#Get line,word and character counts in a file
def readFile():
    filename=input("Enter the filename : ")
    try:
        file = open(filename,"r")
        return file
    except FileNotFoundError:
        print("Error : File not found!")

def getCount():
    file = readFile()
    line_count= 0
    word_count = 0
    character_count = 0
    for i in file:
        line_count+=1
        words = i.split(" ")
        word_count+=len(words)
        for j in words:
            character_count+=len(j)
    file.close()
    return line_count,word_count,character_count

def showOutput():
    line_count,word_count,character_count = getCount()
    print("Details of file : ")
    print("No of lines : ",line_count)
    print("No of Words : ",word_count)
    print("No of Characters : ",character_count)

showOutput()







