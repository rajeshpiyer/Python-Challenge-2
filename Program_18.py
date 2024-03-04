#Python program to for student height record for a school using Class and Objects.
class StudentHeight:
    studentList = []
    def __init__(self,name,rollno,height) -> None:
        self.name = name
        self.rollno = rollno
        self.height = height
        self.studentList.append(self)
    
    def __str__(self) -> str:
        return f"\nRoll No : {self.rollno}\nName : {self.name}\nHeight : {self.height} cm"

def createStudent():
    rollno = input("Enter the Roll No : ")
    name = input("Enter the name : ")
    height = input("Enter the Height(cm) : ")
    student = StudentHeight(name,rollno,height)
    print("Details added Successfully!")

ch='y'
while(ch=='y' or ch=='Y'):
    print("1.Add Student\n2.View Student List")
    choice = int(input("Enter your choice : "))
    if choice==1:
        createStudent()
    elif choice==2:
        for i in StudentHeight.studentList:
            print(i)
    else:
        print("Invalid Choice!!")
    ch = input("Do you wish to go again?(Y/N) : ")

        