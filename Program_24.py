#Rock Paper Scissors
import random

def game():
    input_list = ["Rock","Paper","Scissors"]
    points = int(input("Enter no of points to play : "))
    user_points=0
    cpu_points=0

    i=1
    while(i<=points):

        print(f"\nRound {i} : ")
        for j in input_list:
            print(f"{input_list.index(j)+1}: {j}")

        user_choice = int(input("Enter your choice : "))-1
        while(user_choice<0 or user_choice>2):
            user_choice = int(input("Enter a valid choice : "))-1

        cpu_choice = generate_cpu_choice()-1

        print(f"Your Choice : {input_list[user_choice]}")
        print(f"CPU choice : {input_list[cpu_choice]}")

        if user_choice==0 and cpu_choice==1:
            print("CPU win 1 point!")
            cpu_points+=1
        elif user_choice==0 and cpu_choice==2:
            print("You win 1 point!")
            user_points+=1
        elif user_choice==1 and cpu_choice==0:
            print("You win 1 point!")
            user_points+=1
        elif user_choice==1 and cpu_choice==2:
            print("CPU win 1 point!")
            cpu_points+=1
        elif user_choice==2 and cpu_choice==0:
            print("CPU win 1 point!")
            cpu_points+=1
        elif user_choice==2 and cpu_choice==1:
            print("You win 1 point!")
            user_points+=1
        else:
            print("No Score, Play Again")
            points+=1
        print(f"Scores : You : {user_points}, CPU : {cpu_points}")
        i+=1
    print(f"\nYour Points : {user_points}\nCPU Points : {cpu_points}")
    if cpu_points>user_points:
        print("\nGAME OVER\nCPU WIN!! -- Better Luck Next Time")
    elif user_points>cpu_points:
        print("\nGAME OVER\nYOU WIN!! -- CONGRATULATIONS")
    else:
        print("\nGAME OVER\nSCORES LEVEL!!!!")

def generate_cpu_choice():
    return random.randint(1,3)

ch='y'
while(ch=='y' or ch=='Y'):
    print("-------------------------")
    print("-- ROCK-PAPER-SCISSORS --")
    print("-------------------------")
    game()
    ch = input("Do you wish to go again?(Y/N) : ")
