
WORKFLOW OF PROJECT:
1- Input from user(Rock,paper,scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock = tie
Rock - Rock = paper win
Rock - Scissor = Rock wine

B- paper
paper - paper = tie
paper - Rock = paper win
paper - scissor = Scissor win

C- Scisssor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - paper = Scissor win

"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, paper, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = computer")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Papper":
    if comp_choice == "Scissor":
        print("Scissor cut paper, Computer Win")
    else:
        print("Paper covers rock, You win")

elife user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, You win")
    else:
        print("Rock smashes scissor, Computer win")

