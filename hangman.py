#hangman game

string = "guess_this"
guessed = "_ " * len(string)
guessedList = list(guessed)
guessedLetters = []

maxTries = 10
numTries = maxTries
running = True

while running:
    if guessed.replace(" ", "") == string:
        print("\nEYYY YA BEAT IT!!")
        print("YES IT'S " + string)
        print("Try Again? (y/n): ")
        c = str(input())
        if c.lower() == 'y':
            running = True
            numTries = maxTries
            guessed = "_ " * len(string)
            guessedList = list(guessed)
            guessedLetters = []
        else:
            running = False

    if numTries <= 0:
        print("***GAME OVER***")
        print("Try Again? (y/n): ")
        c = str(input())
        if c.lower() == 'y':
            running = True
            numTries = maxTries
            guessed = "_ " * len(string)
            guessedList = list(guessed)
            guessedLetters = []
        else:
            running = False

    if running:
        print(str(numTries) + " Tries remaining.")
        print(guessed)
        
        letter = input("Next Letter: ")
        if len(letter) != 1 or letter in guessedLetters:
            while len(letter) != 1 or letter in guessedLetters:
                letter = input("Enter a single letter not already guessed, ya dummy!: ").lower()

        guessedLetters.append(letter)
        numTries = numTries - 1
        #see if the letter is in string
        for i in range(len(string)):
            if string[i] == letter:
                guessedList[2 * i] = letter
                guessed = "".join(guessedList)


print("Bye!!")

