#THis is my second try at the game of dice
#Let's try not to screw the fairness of die in this game
import random
faces={1:("┌─────────┐",
          "│         │",
          "│    ●    │",
          "│         │",
          "└─────────┘"),
       2:("┌─────────┐",
          "│ ●       │",
          "│         │",
          "│       ● │",
          "└─────────┘"),
       3:("┌─────────┐",
          "│ ●       │",
          "│    ●    │",
          "│       ● │",
          "└─────────┘"),
       4:("┌─────────┐",
          "│ ●     ● │",
          "│         │",
          "│ ●     ● │",
          "└─────────┘"),
       5:("┌─────────┐",
          "│ ●     ● │",
          "│    ●    │",
          "│ ●     ● │",
          "└─────────┘"),
       6:("┌─────────┐",
          "│ ●  ●  ● │",
          "│         │",
          "│ ●  ●  ● │",
          "└─────────┘"),
       }
i=total=0
def organiser():
    print("\n\n\n\n\n\n")
while True:
    try:
        number_of_die=int(input("Enter the number of die you want to roll"))
        break
    except ValueError or number_of_die==0:
        print("We don't do that here,try again")
while True:
    if i>0:
        while True:
            try:
                number_of_die = int(input("Enter the number of die you want to roll"))
                break
            except ValueError or number_of_die == 0:
                print("We don't do that here,try again")
    total=0
    faces__=[]
    for counter in range(number_of_die):
        faces__.append(random.randint(1,6))
    for line in range(5):#becase our dices are of height 5
            #What we're trying to do is print everything in a horizontal pattern,like first line 1 for all the dices then line 2 and so on till 5,that is the height of the die
        for face in faces__:
            print(faces.get(face)[line],end="")
        print()
    for face in faces__:
        total += face
    print(f"total :{total}")
    i+=1
    roll_again=input("Roll again? (y/n)").lower().strip()
    if roll_again == "y":
        continue
    else:
        break

