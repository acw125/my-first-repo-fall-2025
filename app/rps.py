import random

Resp_T = ""
Resp_I = 0
player = "Input"
Win = 0
Loss = 0
Win_T = 0
Games_T = 0
Games_P = 0
Match_W = 0
Match_T = 0
Match_P = 0
playing = "Yes"
ErrorCheck = False
Winner = 0

PLAYER_NAME = input("Please enter your name: ")

print("Welcome ", PLAYER_NAME, " to my rock, paper, scissors game!")

while playing == "Yes":

    while Winner == 0:

        ErrorCheck = False
        Resp_I = random.randint(1,3)

        if Resp_I == 1:
            Resp_T = "Rock"
#            print(Resp_T)
        elif Resp_I == 2:
            Resp_T = "Paper"
#            print(Resp_T)
        elif Resp_I == 3:
            Resp_T = "Scissors"
#            print(Resp_T)

        while ErrorCheck == False:
            player = input("Rock, Paper, Scissors, SHOOT: ").title()
            print("-------------------------")

            if player == "Rock":
                ErrorCheck = True
                print("Player Input: ", player)
                print("-------------------------")
            elif player == "Paper":
                ErrorCheck = True
                print("Player Input: ", player)
                print("-------------------------")
            elif player == "Scissors":
                ErrorCheck = True
                print("Player Input: ", player)
                print("-------------------------")
            else:
                print("Invalid Input. Try Again")


        print("Computer Input: ", Resp_T)
        print("-------------------------")

        if player == Resp_T:
            print("DRAW")
        elif player == "Rock" and Resp_T == "Scissors":
            Win += 1
            Win_T += 1
            print("Wins: ", Win," Losses: ", Loss)
        elif player == "Scissors" and Resp_T == "Paper":
            Win += 1
            Win_T += 1
            print("Wins: ", Win," Losses: ", Loss)
        elif player == "Paper" and Resp_T == "Rock":
            Win += 1
            Win_T += 1
            print("Wins: ", Win," Losses: ", Loss)
        else:
            Loss += 1
            print("Wins: ", Win," Losses: ", Loss)

        Games_T += 1

        if Win == 3:
            Winner = 1
            Match_W += 1
            Match_T += 1
            print("YOU WIN")
        elif Loss == 3:
            Winner = 1
            Match_T += 1
            print("YOU LOSE")

#   Reset
    Win = 0
    Loss = 0
    ErrorCheck = False

#    ErrorCheck
    while ErrorCheck == False:
        playing = input("Play Again? (Yes or No)").title()

        if playing == "Yes":
            Winner = 0
            ErrorCheck = True
        elif playing == "No":
            ErrorCheck = True
        else:
            print("Invalid Input. Try Again")

print("-------------------------")
print("Thanks For Playing ", PLAYER_NAME, "!")
print("-------------------------")

Games_P = Win_T / Games_T
Match_P = Match_W / Match_T

print("Game Win Percent: ", Games_P)
print("Match Win Percent: ", Match_P)