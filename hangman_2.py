import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''','''
    +---+
    O   |
        |
        |
       ===''','''
    +---+
    O   |
    |   |
        |
       ===''','''
    +---+
    O   |
   /|   |
        |
       ===''','''
    +---+
    O   |
   /|\  |
        |
       ===''','''
    +---+
    O   |
   /|\  |
   /    |
       ===''','''
    +---+
    O   |
   /|\  |
   / \  |
       ===''','''
    +---+
   (O   |
   /|\  |
   / \  |
       ===''','''
    +---+
   (O)  |
   /|\  |
   / \  |
       ===''']
words = {"Colors":"red orange yellow lime green aqua blue indigo purple pink white black brown".split(),"Shapes":"circle line triangle square pentagon hexagon heptagon octagon nonagon decagon".split(),"Fruits":"Apple, orange, banana, lemon, lime, pear, watermelon, grape, blueberry, blackberry, grape, grapefruit, pomegrante, cherry, cantaloupe, mango, strawberry, tomato".split(),"Animals":"ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crab crow deer dog donkey dragon duck eagle falcon ferret fox frog".split()}
def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex],wordKey]
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('You can not do this. Please only enter a single letter.')
        elif guess in alreadyGuessed:
            print("You have already guessed this letter. Choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a real letter (e.g. "a")')
        else:
            return guess
def playAgain():
    print('Do you wish to play again? Answer with a yes or no.')
    return input().lower().startswith('y')

print('H A N G M A N')
difficulty = 'X'
while difficulty not in 'EMH':
    print('Enter difficulty: (E = Easy, M = Medium, H = Hard) --->')
    difficulty = input().upper()

if difficulty == 'M':
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[8]
if difficulty == 'H':
    del HANGMAN_PICS[3]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[8]

missedLetters = ''
correctLetters = ''
secretWord,secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print("The secret word is in the set: " + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters += guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Congratulations!!! You have survived HANGMAN!!! The secret word was"' + secretWord + '"!')
            gameIsDone = True
    else:
        missedLetters += guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses.\n After ' + str(len(missedLetters) + ' missed guesses and ' + str(len(correctLetters) + ' correct guesses; the word was "' + secretWord + '".')))
                gameIsDone = True
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord, secretSet = getRandomWord(words)
            else:
                break