import random


print("Rock Paper Scissor Game \n")

moves = ["rock", "paper", "scissor"]
comp = random.choice(moves)

print("You choose?")
player = input().lower()

choosing = True
while choosing:
    
    if player in moves:
        if player == comp:
            print("Draw. Try again")
            player = input().lower()
            comp = random.choice(moves)
            continue
        elif player == "rock" and comp == "scissor":
            print("You win")
        elif player == "rock" and comp == "paper":
            print("You lose")
        elif player == "paper" and comp == "rock":
            print("You win")
        elif player == "paper" and comp == "scissor":
            print("You lose")
        elif player == "scissor" and comp == "paper":
            print("You win")
        elif player == "scissor" and comp == "rock":
            print("You lose")
        choosing = False 
    else:
        print("Choose again")
        player = input().lower()   