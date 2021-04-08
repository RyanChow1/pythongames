import random
import time

def displayIntro():
    print('''You will choose between 2 dragons. You will visit one or the other's cave. One will give you treasure, and one will eat you.
    Choose wisely.''')

def chooseCave():
    cave = ""
    while cave != '1' and cave != '2':
        print('Which cave will you choose? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print("You approach the cave.")
    time.sleep(2)
    print("It is ominous and scary.")
    time.sleep(2)
    print("SUDDENLY, A LARGE DRAGON JUMPS IN FRONT OF YOU AND OPENS ITS MOUTH...")
    friendlyCave = random.randint(1, 2)
    if chosenCave == str(friendlyCave):
        time.sleep(2)
        print("And he gives you his treasure!!!")
        time.sleep(2)
    else:
        time.sleep(2)
        print("And he gobbles you down whole!!!")
        time.sleep(2)

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Do you want to play again? (Yes or No)")
    playAgain = input()