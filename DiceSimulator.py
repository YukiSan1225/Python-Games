#This is a small project that I can do to test my skills
from random import *
def main():
    print ('Welcome to the Rolling Dice Simulator\n')
    print ('The range will be from 1 to 6 of course. Whenever you are ready\n just hit Enter!.')

    user = input("")
    if user == "":
        DiceRoll()
    else:
        print ("You have not pressed Enter. Restarting program...")
        main()

def DiceRoll():
    print ("Ladies and gentleman, please hold your buts. Rolling Dice now....")
    #Starting the Dice Roll Algorithm
    maxNum = 6
    minNum = 1

    randomNum = randint(minNum, maxNum)

    print ("Oh my goodness, you've just been handed " + str(randomNum) +". I hope this is what you've wanted!")
    print ('\nWanna roll again? Press Enter again if you would like to do it again!')

    tryAgain = input("")
    if tryAgain == "":
        DiceRoll()
    else:
        print ("Thank you!")
        exit()

if __name__ == '__main__':
    main()






