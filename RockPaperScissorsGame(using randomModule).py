#here we tried to create the rock paper scissors game using the random module

import random
l=["rock","paper","scossors"]
computer_count=0
user_count=0

while True:
    user_input=int(input('''
    Game Start......
    1.Yes
    2.No|exit'''))
    if user_input==1:
        for i in range(1,6):
            user_input1=int(input('''
            1.rock
            2.paper
            3.scossors
            
            '''))
            if user_input1==1:
                uchoice="rock"
            elif user_input1=="2":
                uchoice = "paper"

            elif user_input1==3:
                uchoice = "scossors"
            comuter_choice=random.choice(l)
            print(uchoice)
            print(comuter_choice)
            if comuter_choice==uchoice:
                print("computer value",comuter_choice)
                print("user choice",uchoice)
                print("game drow")
                user_count=user_count+1
                computer_count=computer_count+1
            elif (user_input1=="rock" and comuter_choice=="scossors") or (user_input1=="paper" and comuter_choice=="rock") or (user_input1=="scossors" and comuter_choice=="paper"):
                print("computer value", comuter_choice)
                print("user choice", uchoice)
                print("you win")
                user_count=user_count+1
            else:
                print("computer value", comuter_choice)
                print("user choice", uchoice)
                print("computer win")
                computer_count=computer_count+1
        if user_count==computer_count:
            print("final game drow........")
            print("computer score is:=.......",computer_count)
            print("user score is :=........",user_count)

        elif user_count>computer_count:

            print(" finally   you win the game.......")
            print("computer score is:=.......", computer_count)
            print("user score is :=........", user_count)
        else:
            print(" finally   you computer win  the game.......")
            print("computer score is:=.......", computer_count)
            print("user score is :=........", user_count)








    else:
        break




















