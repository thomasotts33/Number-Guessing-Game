import random

###---Functions---###

def getDifficulty():
    while True:
        difficulty = int(input("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n\n"))
        if (difficulty > 3 or difficulty < 1):
            print("\nInvalid input. Please select a valid difficulty level.")
        else:
            return difficulty

def getChances(num):
    chances = 0
    if difficulty == 1:
        chances = 10
        return chances
    elif difficulty == 2:    
        chances = 5
        return chances
    elif difficulty == 3:
        chances = 3
        return chances

#Game function
#Loops through while guesses are still available 
#and random number has not been guessed
def playGame(chances):
    # print(f"In game with {chances} chances")
    gameChances = chances
    number = random.randint(1,100)
    # print(number)
    guess = ' '
    while (gameChances > 0):
        guess = int(input(f"Enter your guess below: ({gameChances} guesses left)\n"))

        if (guess == number):
            print("\nYou Win!\n")
            print(f"You guessed the number in {(chances - gameChances) + 1} guesses")
            gameChances = -1
        else:
            gameChances -= 1
            if (guess < number):
                print(f"\nNumber is greater than {guess}")
            else:
                print(f"\nNumber is less than {guess}")
    if (gameChances == 0 and guess != number):
        print("\nYou Lose... womp womp\n")
def nextRound():
    print("\nWould you like to play again? (y/n)\n")
    if (input().lower() == 'y'):
        playAgain = True
        return playAgain
    else:
        print("\nThanks for playing!")
        playAgain = False
        return playAgain
###---Start---###

playAgain = True
while (playAgain == True):
    print("\nWelcome to the Number Guessing Game!\n")
    difficulty = getDifficulty()
    chances = getChances(difficulty)
    playGame(chances)
    playAgain = nextRound()





# You have 5 chances to guess the correct number.

