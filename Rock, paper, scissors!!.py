import time
import random
#This is a game of rock, paper, scissors
Replay=True
while Replay:
    print("This is a game of Rock,Paper,Scissors")
    their_choice=""
    print("~~~🪨🪨Rock🪨🪨~~~")
    time.sleep(1)
    print("~~~📃📃Paper📃📃~~~")
    time.sleep(1)
    print("~~~✂️✂️Scissors✂️✂️~~~")
    time.sleep(1)
    computers_choice=("ROCK", "PAPER", "SCISSORS")
    while True:
        try:
            their_choice=input("(Your choice) :").upper().strip()
            if their_choice=="ROCK" or their_choice=="PAPER" or their_choice=="SCISSORS":
                break
            else:
                print("That is not a valid choice!!!")
                print("Try again......Cheater😒😒")
        except not their_choice.isalpha():
            print("That is not a valid choice!!!")
            print("Try again......Cheater😒😒😒")
    #computer_choice=computers_choice[random.randint(0,len(computers_choice)-1)] can be a possible wy too!!
    computers_choice=random.choice(computers_choice) #Another way
    print("~~~Shoo!!~~~")
    time.sleep(1)
    print(f"~~Your choice :{their_choice}~~\n~~Computer's choice :{computers_choice}~~")
    if their_choice==computers_choice:
        print("DRAW!!")
        play_again=input("Would you like to play again? (y/n)").lower()
        if play_again=="y":
            continue
        else:
            break
    if computers_choice=="ROCK" and their_choice=="PAPER":
        print("You win!")
        continue
    elif computers_choice=="PAPER" and their_choice=="SCISSORS":
        print("You win!")
        play_again = input("Do you want to play again? (Y/N) :").lower().strip()
        if play_again=="n":
            Replay=False
        continue
    elif computers_choice=="SCISSORS" and their_choice=="ROCK":
        print("You win!")
        play_again = input("Do you want to play again? (Y/N) :").lower().strip()
        if play_again=="n":
            Replay=False
        continue
    else:
        print("You lose!")
    play_again=input("Do you want to play again? (Y/N) :").lower().strip()
    if play_again=="y":
        continue
    else:
        Replay=False


