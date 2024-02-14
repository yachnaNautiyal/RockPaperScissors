import random




# function to implete the logic of rock paper and scissors
def compute():
    computer_input= random.choice(options)
    print("Computer Chose: ", computer_input)

    if user_input==computer_input:
        print("Oh no.. It's a tie.")
    elif user_input=="rock":
        if computer_input=="scissors":
            print("Rock smashes scissors..!! You Win...!!")
        else:
            print("Computer wins...!!")
            
    elif user_input=="paper":
        if computer_input=="rock":
            print("Paper covers rock..!! You Win...!!")
        else:
            print("Computer wins...!!")
    
    elif user_input=="scissors":
        if computer_input=="paper]":
            print("Scissors cut paper..!! You Win...!!")
        else:
            print("Computer wins...!!")
    
        
    
# Loop would let the user play the game again and again.
PlayAgain="Y"

while (PlayAgain=="Y"):

    options= ["rock", "paper", "scissors"]

    user_input= input("Enter your choice (rock/paper/scissors): ")
    user_input= user_input.lower().strip()
    if user_input in options:
        print("You chose: " +user_input )
        compute()

    else:
        print("Please choose right option")

    PlayAgain=(input("Do you want to play again (Y/N): ")).upper().strip()
    print("--------------------------------------------------")

