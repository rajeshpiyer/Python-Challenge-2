def readFile():
    filename=input("Enter the filename : ")
    try:
        file = open(filename,"r")
        return file
    except FileNotFoundError:
        print("Error : File not found!")

def count_Occurence():
    occurence_dict={}
    file=readFile()
    for i in file:
        words = i.split(" ")
        for j in words:
            if occurence_dict.get(j.lower())==None:
                occurence_dict[j.lower()]=1
            else:
                occurence_dict[j.lower()]+=1
    for i in occurence_dict:
        print(f"{i} : {occurence_dict.get(i)}")

count_Occurence()

