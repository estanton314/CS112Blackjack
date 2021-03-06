#CS-112 Midterm 2 Project
#by Ellen Stanton

#main function
def main():
    
    instructions()
    firstGuesser, secondGuesser = whoGuessesFirst()
    secretWord = getSecretWord()

    #initializes number of wrong guesses, list of wrong guesses, word progress,
        #number of total guesses, and the snowman
    wrongGuessCount = 0
    wrongGuessList = []
    wordProgress = ["_"] * len(secretWord)
    guesses = 0
    snowman = [[" "," "," "],[" "," "," "],[" "," "," "],["~","~","~"]]

    #loop runs if turns haven't run out and word hasn't been guessed
    while wrongGuessCount<8 and "_" in wordProgress:
        currentGuesser,otherGuesser = whoGuessesNow(guesses,firstGuesser,\
                                                    secondGuesser)

        #shows wrong guesses and word progress so far
        if wrongGuessCount>0:
            print("The incorrect guesses so far are:")
            print(wrongGuessList, "\n")
        print(wordProgress, "\n")

        guess = getGuess(wrongGuessList,wordProgress)

        #tells if guess is correct
        if guess in secretWord:
            print("You guessed a letter correctly!\n")
            wordProgress = fillInBlank(secretWord,guess,wordProgress)

        #adds guess to list of wrong guesses if incorrect, increments number of
            #wrong guesses and total guesses
        else:
            print("You did not guess a correct letter.\n")
            wrongGuessCount+=1
            wrongGuessList.append(guess)
        guesses+=1

        snowman = drawSnowman(snowman,wrongGuessCount)
        print("Here's your snowman so far:")
        printPretty(snowman)
        print()
        
    report(wrongGuessCount,secretWord,currentGuesser)


#function prints instructions to the screen
def instructions():
    print("You are now going to play Snowman!\nYou will have to guess my secret\
 word, one letter at a time. When you guess a right letter, I'll show you \
 where it is in the word, and what spaces you still have to fill. If you \
 guess a wrong letter, the snowman will gain another body part. If all 8 \
 body parts are drawn, you both lose. Try to guess the last right letter \
 and win!\nIt's tough, so... good luck!")
    enter = input("Hit Enter to continue...")
    print()

#function randomly decides which of the two players guess first
    #output is who guesses first and who guesses second
def whoGuessesFirst():
    playerOneName = input("What is the name of one of the players? ")
    playerTwoName = input("What is the name of the other player? ")
    print("Hi " + playerOneName + " and " + playerTwoName + "!\n")
    players = [playerOneName, playerTwoName]
    import random
    firstGuesser = random.choice(players)
    if firstGuesser == playerOneName:
        secondGuesser = playerTwoName
    else:
        secondGuesser = playerOneName
    print(str(firstGuesser) + " will guess first.")
    return(firstGuesser,secondGuesser)

#function chooses secret word from file of potential options
    #output is the secret word
def getSecretWord():
    import random
    f = open("secretwordlist.py","r")
    words = f.readlines()
    secretWords = []
    for word in words:
        word=word.strip()
        secretWords.append(word)
    secretWord = random.choice(secretWords)
    return secretWord

#function determines who's guessing for each individual turn
    #inputs are number of guesses, who guessed first, and who guessed second
    #output is who guesses currently and who guesses next
def whoGuessesNow(guesses,firstGuesser,secondGuesser):
    if guesses%2 == 0:
        print(str(firstGuesser) + ", it's your turn.\n")
        currentGuesser = firstGuesser
        otherGuesser = secondGuesser
    else:
        print(str(secondGuesser) + ", it's your turn.\n")
        currentGuesser = secondGuesser
        otherGuesser = firstGuesser
    return(currentGuesser, otherGuesser)

#function prompts the user for a guess and ensures entries are valid
    #inputs are wrong guesses so far and
        #progress of word so far, which contains right guesses
    #output is the valid guess
def getGuess(wrong,progress):
    guessAgain = "yes"
    while guessAgain == "yes":
        guess = input("Guess a letter that you think is in the secret word. ")
        if guess in wrong or guess in progress:
            print("You already guessed " + guess + ". Guess again.\n")
        elif not guess.isalpha():
            print("You must enter a valid letter as input. Guess again.\n")
        elif len(guess)!=1:
            print("Your guess must be one character only. Guess again.\n")
        else:
            guess = guess.lower()
            guessAgain = "no"
    return guess

#function adds correct guesses to list of progress towards the word
    #inputs are the secret word, the guess, and the word progress so far
    #output is the updated word progress
def fillInBlank(secretWord,guess,wordProgress):
    for i in range(len(secretWord)):
        if secretWord[i] == guess:
            wordProgress[i] = guess
    return(wordProgress)

#function adds a body part to the snowman for each wrong guess
    #input is current snowman number of wrong guesses
    #output is updated grid of snowman body parts
def drawSnowman(snowman,wrongGuessCount):
    if wrongGuessCount == 1:
        snowman[0][1] = "("
    elif wrongGuessCount == 2:
        snowman[0][1] = "()"
    elif wrongGuessCount == 3:
        snowman[1][1] = "("
    elif wrongGuessCount == 4:
        snowman[1][1] = "()"
    elif wrongGuessCount == 5:
        snowman[2][1] = "("
    elif wrongGuessCount ==6:
        snowman[2][1] = "()"
    elif wrongGuessCount ==7:
        snowman[1][0] = "/"
    elif wrongGuessCount ==8:
        snowman[1][2] = "\\"
    return snowman

#function turns snowman grid into something to be printed prettily
    #input is grid of snowman
#this code courtesy of Nanette!
def printPretty(grid):
    numOfrows = len(grid)
    rowLength = len(grid[0])
    for r in range(numOfrows):
        for c in range(rowLength):
            print(" " + str(grid[r][c]), end="")
        print()

#function reports if the players lost together, or if one of them one
    #inputs are number of wrong guesses, secret word, and
        #who took the last guess
def report(wrongGuessCount,secretWord,currentGuesser):
    if wrongGuessCount == 8:
        print("I'm sorry, you didn't guess the secret word before losing \
your 8 lives. It was \"" + secretWord + "\"")
    else:
        print(currentGuesser + ", you guessed the secret word, \"" + secretWord\
        + "\"! Congratulations.")
