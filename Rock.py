import random
R = "rock"
P = "paper"
S = "scissors"
list = [R, P, S]
computer = random.choice(list)
print(computer)
user = input("play now !!! ")
def balance():
    if user == "P":
        return P
    elif user == "S":
        return S
    elif user == "R":
        return R

First = balance()
print(First)

def pick():
    CPU = computer
    user = First
    if user == computer:
        while user == computer:
            print("This is a tie \n You played ", user,"and Computer played ", computer)
            user = input("play now !!! ")
    elif user not in (R, S, P):
        while user not in (R, S, P):
            print("Error... try again")
            user = input("play now !!! ")
    elif (user == R and computer == S) or (user == P and computer == R) or (user == S and computer == P):
        print("You win !! \n You played ", user, "and computer played ", computer)
    else:
        print("You lose !! \n You played ", user, "and computer played ", computer, "Therefore computer wins")

pick()
