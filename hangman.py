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
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crab crow deer dog donkey dragon duck eagle falcon ferret fox frog goat gold goose hawk ice jungle kyanite lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pig pigeon poo python rabbit rat raven rhino salmon seal shark sheep silver skunk sloth snake spider stone stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]
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
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
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
                secretWord = getRandomWord(words)
            else:
                break