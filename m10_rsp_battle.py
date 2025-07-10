import random
import datetime

print("""Winning Rules of the Rock Paper Scissors game as follows:
1. Rock vs Paper -> Paper wins
2. Rock vs Scissors -> Rock wins
3. Paper vs Scissors -> Scissors wins
""")

start_time = datetime.datetime.now()
print("Game started at:", start_time)

while True:
    print("""Enter choice:
    1. Rock
    2. Scissors
    3. Paper """)

    choice = int(input("Your turn: "))
    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Scissors"
    else:
        choice_name = "Paper"

    print("Your choice is: " + choice_name)

    print("\nNow it's the computer's turn")
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Scissors"
    else:
        comp_choice_name = "Paper"

    print("Computer choice is: " + comp_choice_name)
    print("Battle : " + str(choice_name) + " VS " + str(comp_choice_name))

    if comp_choice != choice:
        if (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
            print("Rock wins")
            result = "Rock"
        elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
            print("Paper wins")
            result = "Paper"
        else:
            print("Scissors wins")
            result = "Scissors"

        if result == choice_name:
            print("<== User wins ==>")
        else:
            print("<== Computer wins ==>")
    else:
        print("<== Tie ==>")

    response = input("\nDo you want to play again? (Y/N): ")
    if response.lower() == "n":
        break

end_time = datetime.datetime.now()

duration = end_time - start_time

print("\nThanks for playing!")
print("Game started at:", start_time)
print("Game ended at:", end_time)
print("Duration:", duration)