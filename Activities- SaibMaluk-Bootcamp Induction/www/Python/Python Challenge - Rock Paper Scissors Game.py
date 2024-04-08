# Python Challenge - Rock Paper Scissors Game

import random

while True:
    userChoice = input("Enter a choice (rock, paper, scissors): ")
    Choices = ["rock", "paper", "scissors"]
    computerChoice = random.choice(Choices)
    print(f"\nYou chose {userChoice}, computer chose {computerChoice}.\n")

    if userChoice == computerChoice:
        print(f"Both players selected {userChoice}. It's a tie!")
    elif userChoice == "rock":
        if computerChoice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif userChoice == "paper":
        if computerChoice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif userChoice == "scissors":
        if computerChoice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
