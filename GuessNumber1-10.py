playerOneName = input("What is the name of one of the players? ")
playerTwoName = input("What is the name of the other player? ")
for count in range(1,4):
    import random
    winningNumber = random.randrange(1, 11)
    players = [playerOneName, playerTwoName]
    firstGuesser = random.choice(players)
    if firstGuesser == playerOneName:
        secondGuesser = playerTwoName
    else:
        secondGuesser = playerOneName
    print(str(firstGuesser) + " will guess first.")
    guesses = 0
    while guesses<6:
        if guesses%2 == 0:
            print(str(firstGuesser) + ", it's your turn.")
            currentGuesser = firstGuesser
            otherGuesser = secondGuesser
        else:
            print(str(secondGuesser) + ", it's your turn.")
            currentGuesser = secondGuesser
            otherGuesser = firstGuesser
        guessedNumber = int(input("Guess a number in the range 1-10. Or, to \
give up, guess 0. "))
        if 1 <= guessedNumber <= 10:
            if guessedNumber == winningNumber:
                print("Congratulations " + currentGuesser + "! You guessed \
the right number. You win game number " + str(count) +"!")
                guesses=6
            elif guessedNumber < winningNumber:
                print("The number you guessed is too low. ")
                guesses+=1
                if guesses == 6:
                  print(playerOneName, "and", playerTwoName, ", both of you \
lose.")
            else:
                print("The number you guessed is too high. ")
                guesses+=1
                if guesses == 6:
                  print(playerOneName, "and", playerTwoName, ", both of you \
lose.")
        elif guessedNumber == 0:
            print(str(currentGuesser) + " gave up. ")
            print(str(otherGuesser) + " wins!")
            guesses = 6
        else:
            print("You entered an invalid guess.")
            guesses+=1
            if guesses == 6:
                  print(playerOneName, "and", playerTwoName, ", both of you \
lose.")
