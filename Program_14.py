#Add, Overwrite, Read notes

class Notes:
    filename = "Notes.txt"

    def read(self):
        print("-- VIEW NOTES --")
        file=open(self.filename,"r")
        for i in file:
            print(i)
        print("Sorry, File not Created yet !!\n Choose 'write' option to create notes.")
        file.close()

    def write(self):
        file=open(self.filename,"w")
        sentence = input("Enter the notes to write to file : ")
        file.write(sentence)
        file.close()
    
    def append(self):
        file=open(self.filename,"a")
        sentence = input("Enter the notes to add to the file : ")
        file.write(sentence)
        file.close()

note = Notes()
choice=0
while(choice!=4):
    try:
        print("-- NOTES EDITOR --")
        print("\n1.Create/Overwrite\n2.Append\n3.Read\n4.Exit")
        choice=int(input("Choice : "))
        if choice==1:
            note.write()
        elif choice==2:
            note.append()
        elif choice==3:
            note.read()
    except FileNotFoundError:
        print("Sorry, File not Created yet !!\n Choose 'Create' option to create notes.")
        continue

