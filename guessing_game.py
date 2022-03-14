# importing random module
import random

print("Welcome to the Guessing Game, Where you can test your luck against the computer")

choice = input("Do you dare to play? ")


# if the player don't want to play the game quit
if choice.lower() != "yes":
    choice_quit = input("Do you want to Quit? (y/n) ")
    if choice_quit == "y":
        quit()


# if the player want to play the game
print("Thank you Player for playing the Game")

# difficulties level
lvl_easy = 10
lvl_intermediate = 20
lvl_expert = 30
lvl_veteran = 50

print("Which level do you want to play?\n1.Easy(1-10)\n2.Intermediate(1-20)\n3.Expert(1-30)\n4.Veteran(1-50)\n\nIf you want to quit than please choose -1\n\n")
lvl = int(input("Enter your choice: "))

# lvl easy
if lvl == 1:
    print("You've chosen difficulty level Easy")
    # starts from 0 and end on n+1
    target_number = random.randrange(lvl_easy + 1)
    print("\nGuess a number between 1-10 to Win\n")
    guess = int(input(("Enter your guess: ")))
    guessed = 0
    while target_number != guess:
        guessed += 1
        if guess > target_number:
            guess = int(input("You've guessed too High. Please guess again: "))
        elif guess < target_number:
            guess = int(input("You've guessed too Low. Please guess again: "))
        elif guess == -1:
            quit()
    else:
        print(f"You WIN!!\nYou've Guess {guessed} times.")

# lvl intermediate
elif lvl == 2:
    print("You've chosen difficulty level Intermediate")
    # starts from 0 and end on n+1
    target_number = random.randrange(lvl_intermediate + 1)
    print("\nGuess a number between 1-20 to Win\n")
    guess = int(input(("Enter your guess: ")))
    guessed = 0
    while target_number != guess:
        guessed += 1
        if guess > target_number:
            guess = int(input("You've guessed too High. Please guess again: "))
        elif guess < target_number:
            guess = int(input("You've guessed too Low. Please guess again: "))
        elif guess == -1:
            quit()
    else:
        print(f"You WIN!!\nYou've Guess {guessed} times.")


# lvl expert
elif lvl == 3:
    print("You've chosen difficulty level Expert")
    # starts from 0 and end on n+1
    target_number = random.randrange(lvl_expert + 1)
    print("\nGuess a number between 1-30 to Win\n")
    guess = int(input(("Enter your guess: ")))
    guessed = 0
    while target_number != guess:
        guessed += 1
        if guess > target_number:
            guess = int(input("You've guessed too High. Please guess again: "))
        elif guess < target_number:
            guess = int(input("You've guessed too Low. Please guess again: "))
        elif guess == -1:
            quit()
    else:
        print(f"You WIN!!\nYou've Guess {guessed} times.")


# lvl veteran
elif lvl == 4:
    print("You've chosen difficulty level Veteran")
    # starts from 0 and end on n+1
    target_number = random.randrange(lvl_veteran + 1)
    print("\nGuess a number between 1-50 to Win\n")
    guess = int(input(("Enter your guess: ")))
    guessed = 0
    while target_number != guess:
        guessed += 1
        if guess > target_number:
            guess = int(input("You've guessed too High. Please guess again: "))
        elif guess < target_number:
            guess = int(input("You've guessed too Low. Please guess again: "))
        elif guess == -1:
            quit()

    else:
        print(f"You WIN!!\nYou've Guess {guessed} times.")

elif lvl == -1:
    quit()
