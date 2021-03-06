import random

class Card():
    
    def __init__(self,cardNum):
        #initiates attributes of card object
        self.cardNum = cardNum
        self.suit = self.getCardSuit(cardNum)
        self.rank = self.getCardRank(cardNum)
        self.bjValue = self.getbjValue(cardNum)

    def __str__(self):
        #returns attributes of card
        return("\nCard num: " + str(self.cardNum) + "\n" + \
               self.suit + self.rank + "\nblackjack value: " + \
               str(self.bjValue))
        
    def getCardSuit(self,cardNum):
        #gets suit of card from cardNum
        cardSuits = ["♣","♢","♡","♠"]
        suitIndex = cardNum//13
        return(cardSuits[suitIndex])
    
    def getCardRank(self,cardNum):
        #gets rank of card from cardNum
        cardRanks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        rankIndex = (cardNum%13)
        return(cardRanks[rankIndex])

    def getbjValue(self,cardNum):
        #gets blackjack value of card from cardNum
        #assigns aces 1, they can be made 11 during gameplay
        if (cardNum % 13 + 1) < 10:
            value=(cardNum%13)+1
        else:
            value=10
        return(value)


class Player():
    
    def __init__(self,n):
        #initiates attributes of player object
        self.name = n
        self.hand = []
        self.handValue = 0
        self.gamesWon = 0
        
    def __str__(self):
        #returns attributes of player 
        return("\n" + str(self.name) + "\nhand value: " + str(self.handValue) \
               +"\ngames won: " + str(self.gamesWon))


def main():
    #main function runs blackjack games between two players
    
    instructions()

    #DEALING

    #initializes two player objects
    name1 = input("What's the name of the first player? ")
    name2 = input("What's the name of the second player? ")
    player1 = Player(name1)
    player2 = Player(name2)

    #LCV: again
    again = "Y"
    while again == "Y":

        #initializes 52 card deck, two 2-card hands
        deck = makeADeckOf52()
        player1.hand,deck = dealAHand(deck)
        player2.hand,deck = dealAHand(deck)

        #resets hand values from previous games
        player1.handValue = 0
        player2.handValue = 0

        #PLAYING

        #run turn for player1
        print()
        print(player1.name + ", it's your turn.")
        deck,player1.handValue = turn(deck,player1)

        #run turn for player2
        print()
        print(player2.name + ", it's your turn.")
        deck,player2.handValue = turn(deck,player2)

        #who won individual game
        report(player1,player2)

        again = input("\nWould you like to play again? Y/N ")

    #overall winner
    print(player1.name + " won " + str(player1.gamesWon) + " games.")   
    print(player2.name + " won " + str(player2.gamesWon) + " games.")
    if player1.gamesWon > player2.gamesWon:
        print(player1.name + " is the overall winner!")
    elif player1.gamesWon == player2.gamesWon:
        print(player1.name + " and " + player2.name + " tied.")
    else:
        print(player2.name + " is the overall winner!")


def instructions():
    #input: none
    #output: none
    #process: prints instructions for blackjack
    print("Two players will now play blackjack. For your turn you'll get two \
cards and have to repeatedly choose if you'd like to get another, with the \
goal of the value of your hand equaling 21 or getting as close to 21 as \
possible without going over. A card's value is either the number on it, or \
10 if it's a face card, or if it's an ace you can choose between 1 and 11. \
Your turn ends when you choose not to receive a new card, or you get \
blackjack (21), or you go over 21. The player with the best blackjack score \
wins. Good luck!\n")


def makeADeckOf52():
    #code courtesy of Nanette
    #input: none
    #output: a list of 52 card objects in random order
             #A,2-10,J,Q,K for clubs, diamonds, hearts, spades
    #process: generate 52 card objects associated with numbers 0-51, shuffle
    #debug: deal a smaller deck by making NUM_OF_CARDS_IN_DECK smaller
    NUM_OF_CARDS_IN_DECK=52
    deck = []
    #LCV: the length of the deck
    for i in range (NUM_OF_CARDS_IN_DECK):
        deck.append(Card(i))
    random.shuffle(deck)
    return(deck)


def turn(deck,player):
    #input: deck of cards, current player object
    #output: smaller deck, blackjack value of player's hand
    #process: hand is dealt, player takes new cards until value goes over 21
              # or they decide to stop

    #updates player on hand
    player.handValue = progressUpdate(player)

    #checks initial hand to see if loop for more cards should be entered
    if player.handValue == 21:
        print("Perfect, you got blackjack!")
        keepGoing = "N"
    else:
        keepGoing = input("Would you like to get another card? Y/N ")
    
    #loop to get more cards
    #LCV: keepGoing and player.handValue
    while keepGoing == "Y" and player.handValue<21:
        player.hand.append(deck.pop())
        player.handValue = progressUpdate(player)
        print()
        if player.handValue > 21:
            print("You can't get another card because your black jack value is\
 greater than 21.")
        elif player.handValue == 21:
            print("Perfect, you got blackjack!")
        else:
            keepGoing = input("Would you like to get another card? Y/N ")

    #shows final hand value at end of turn
    print("\nYour final hand value is " + str(player.handValue))
    return(deck,player.handValue)


def dealAHand(deck):
    #input: deck (random list of 52 card objects)
    #output: modified deck with two cards removed,
             #hand (a list of two cards, taken from the deck)
    #process: pop method removes cards, append method adds them to new list
    hand = []
    hand.append(deck.pop())
    hand.append(deck.pop())
    return(hand,deck)


def progressUpdate(player):
    #input: player object
    #output: none
    #process: prints cards in hand and total blackjack value
    print("\nThe cards in your hand are:")
    displayHand(player.hand)
    player.handValue = bjHandValue(player)
    print("The blackjack value of your hand is: " + str(player.handValue))
    return(player.handValue)


def bjHandValue(player):
    #input: player object
    #output: the blackjack value of their hand
    #process: blackjack value of each card in hand is found by calling on object
              #attribute for new cards and adding values to the sum,
              #aces are optionally 1 or 11

    #when hand has just been dealt
    if len(player.hand) == 2:
        for newCard in player.hand:
            if newCard.cardNum != 0 and newCard.cardNum!=13 and \
               newCard.cardNum!=26 and newCard.cardNum!=39:
                player.handValue+= newCard.bjValue
            elif player.handValue > 11:
                player.handValue+=newCard.bjValue
            else:
                ace = input("You have an ace. These usually have a blackjack \
value of 1, but you are allowed to make it have a value of 11, since that \
doesn't cause you to go over 21. Would you like it to be 11 instead of 1? Y/N ")
                if ace == "Y":
                    player.handValue+=11
                else:
                    player.handValue+=1

    #when adding a new card to the existing hand
    else:
        newCard = player.hand[len(player.hand)-1]
        if newCard.cardNum != 0 and newCard.cardNum!=13 and newCard.cardNum!=26\
            and newCard.cardNum!=39:
            player.handValue+= newCard.bjValue
        elif player.handValue > 11:
            player.handValue+=newCard.bjValue
        else:
            ace = input("You have an ace. These usually have a blackjack \
value of 1, but you are allowed to make it have a value of 11, since that \
doesn't cause you to go over 21. Would you like it to be 11 instead of 1? Y/N ")
            if ace == "Y":
                player.handValue+=11
            else:
                player.handValue+=1
    
    return(player.handValue)


def displayHand(hand):
    #input: hand (list of cards)
    #output: none
    #process: prints rank and suit of each card in hand
    for card in hand:
         print(card.suit + card.rank)


def report(player1,player2):
    #input: two player objects
    #output: none
    #process: prints which player wins game, or if they tie, or they both lose
    value1 = player1.handValue
    value2 = player2.handValue
    print()
    if value1 <= 21:
        if value1>value2:
            print(player1.name + " is the winner of this game!")
            player1.gamesWon+=1
        elif value1 < value2 <=21:
            print(player2.name + " is the winner of this game!")
            player2.gamesWon+=1
        elif value1 == value2:
            print("You two tied this game!")
        else:
            print(player1.name + " is the winner of this game!")
            player1.gamesWon+=1
    elif value1>21:
        if value2<=21:
            print(player2.name + " is the winner of this game!")
            player2.gamesWon+=1
        else:
            print("Both of you lost this game.")
