#QUIZ GAME in Python
import os

class Quiz:
    questions = []
    
    def __init__(self,question,a,b,c,d,answer) -> None:
        self.question = question
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.answer = answer
        self.questions.append(self)
    
    def showquestion(self):
        print(self.question)
        print(f"A: {self.a}\nB: {self.b}\nC: {self.c}\nD: {self.d}")
    
    def checkAnswer(self,choice):
        return self.answer.lower()==choice.lower()
    
    
def createQuiz():
    ch='y'
    while(ch=='y' or ch=='Y'):
        print("-- Create New Question --")
        question = input("Enter the Question : ")
        print("Enter the options : ")
        a = input("Option A : ")
        b = input("Option B : ")
        c = input("Option C : ")
        d = input("Option D : ")
        answer = input("Answer (A/B/C/D) : ")
        quiz1 = Quiz(question,a,b,c,d,answer)
        ch = input("Do you wish add another question?(Y/N) : ")

def playGame():
    if Quiz.questions==[]:
        print("Sorry, Question set is empty!\nCreate questions to play quiz!")
    else:
        points = 0
        for i in Quiz.questions:
            print(f"Question : {Quiz.questions.index(i)+1}")
            i.showquestion()
            answer = input("Enter your answer : ")
            if i.checkAnswer(answer):
                print("Yes! Correct Answer")
                points+=1
            else:
                print("!Wrong Answer!")
        percentage = (points/len(Quiz.questions))*100
        print(f"Your Score : {percentage}%")     

def game():
    print("---------------")
    print("-- QUIZ GAME --")
    print("---------------")
    print("1.Create Quiz\t\t2.Play Quiz")
    choice = int(input("Enter your choice : "))
    if choice==1:
        createQuiz()
        os.system('cls' if os.name == 'nt' else 'clear')
        playGame()
    elif choice==2:
        playGame()
    else:
        print("Invalid Choice !")

ch='y'
while(ch=='y' or ch=='Y'):
    os.system('cls' if os.name == 'nt' else 'clear')
    game()
    ch = input("Do you wish to continue?(Y/N) : ")
