import random

#Getting the player's name and welcoming the player into the game with instructions.
player = input("What is your name ... ")
print("You are welcome ", player)
print(
    """
    This is a rock paper scissors game !!
    R - Rock
    P - Paper
    S - Scissors
    Choose R/ P/ S to play
    Play on!!
    """
)

# Setting up the Global variable
R = "Rock"
S = "Scissors"
P = "Paper"
item = [R, S, P]

#Setting up the player
def user():
    user = input("Play here .. ").upper()
    if user == "P":
        return P
    elif user == "S":
        return S
    elif user == "R":
        return R
    else:
        while user not in ("R", "S", "P"):
            print("Invalid choice ... try again ")
            user = input("Play here... ").upper()
            if user == "P":
                return P
            elif user == "S":
                return S
            elif user == "R":
                return R
    
fri = user()

#Setting up the computer
def com():
    computer = random.choice(item)
    return computer
sec = com()

#Setting up the game
def game():
    CPU = sec
    user = fri
    if user == CPU:
        while user == CPU:
            print("This is a tie you played ", user, "and computer played ", CPU)
            user = input("Play here .. ").upper()
            #return fri

    elif (user == R and CPU == S) or (user == S and CPU== P) or (user == P and CPU == R ):
        print("You won by playing", user, "and Computer played ", CPU)
    
    else:
        print("Computer won by playing ", CPU, "and you played ", user)
game()

#Kindly enjoy your game