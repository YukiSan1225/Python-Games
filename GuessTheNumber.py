#Guess The Number &copy Damien Burks 2018
from random import *

maxNum = 10
minNum = 1
def GuessTheNumber():
    print ("Generating the Random Number...")
    #Generate random number algorithm
    randomNum = randint(minNum,maxNum)

    number = input("Guess the Number? ")
    number = int(number)
    if number == randomNum:
        print ("Awesome! You've guessed the number. You win!")
        print ("Wnat to play again?\n Press Enter for yes, type N for no.")
        user = input("")
        if user == "":
            GuessTheNumber()
        else:
            print("Well thanks for playing! Bye Bye!")
            exit()
    elif number > 10 or number < 1:
        print("This number is out of range. Please try again.")
    else:
        print("That's not correct. Better luck next time!")
        exit()

def main():
    print("Welcome to Guess The Number!")
    print("\nThe range that we have today is from " + str(minNum) + " to " + str(maxNum) + ". You'll have to guess the number based on that range."
                                                                                 "Are you ready?")
    print("\n\nLet the GAMES BEGIN!")
    GuessTheNumber()

if __name__ == '__main__':
    main()