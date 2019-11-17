from random import shuffle, choice

global leftCardsNumber
global playgroundsCards
global cards
cards = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10,'J': 11, 'Q': 12, 'K': 13, 'A': 14}

playgroundsCards = []

def printInfo():
    '''Prints all the avaliable info'''

    print(f"*Deck: {deck}\n\n*Left cards number: {leftCardsNumber}\n\n*Trump is {trump} \n\n*Player's deck: {playersDeck}\n\n*Computer's deck: {computersDeck}")

#Function which declare playground of the game
def playground(part, partsCard):#,isNotPlayground):
    '''Game\'s playground'''

#    if isNotPlayground:
#      print('This is the playground: \n\n')
#      isNotPlayground = False

    print(part, ":", partsCard)

    defend(partsCard, computersDeck)

#first
def makeDeck():
    '''Creates and shuffles the deck and declares the trump'''

    global deck
    global trump

    deck = []
    suits = ['♠','♡','♢','♣']

    trump = choice(suits)

    for suit in suits:
        for card in cards:
            deck.append(suit+card)

    shuffle(deck)

#second
def distinguishCard():
    '''Distinguishes decks'''

    global playersDeck
    global computersDeck

    playersDeck = [deck.pop() for i in range(6)]
    computersDeck = [deck.pop() for i in range(6)]

#third
def attack(part,partsDeck):
    '''Player\'s attack'''

    #isNotPlayground = True
    partsDeckLength = len(partsDeck)

    while True:
        index = int(input(f"Please choose the card you want to attack, just send the number from 1 till {partsDeckLength}\n>"))
        index -= 1
        if index <= partsDeckLength:
            break

    chosenCard = partsDeck[index]
    playersDeck.pop(index)
    playgroundsCards.append(chosenCard)
    playground(part,chosenCard)


def popAndAppend(card):
    '''Pops card from the deck and appends it into the playgrounds cards, and then prints the output'''
    cardsIndex = computersDeck.index(card)
    defend = computersDeck.pop(cardsIndex)
    playgroundsCards.append(defend)
    playground('C', card)

def rightCardChecker(playersSuit, playersValue, computersDeck):
    '''Check if there is any avaliable card or not and prints the outcome'''
    for card in computersDeck:
        compsCardsSuit = card[0]
        compsCardsValue = int(cards.get(card[1]))
        rightCard = compsCardsSuit == playersSuit and compsCardsValue > playersValue
        if rightCard:
            popAndAppend(card)
            break
        elif compsCardsSuit == trump:
            if compsCardsSuit == playersSuit and compsCardsValue > playersValue:
                popAndAppend(card)
                break
            else:
                popAndAppend(card)
                break
    else:
            print("I cannot defend, so i'm gonna take that card")

def defend(partsCard, computersDeck):
    """Defendfunction from the side of the computer"""
    playersSuit = partsCard[0]
    playersValue = int(cards.get(partsCard[1]))

    rightCardChecker(playersSuit, playersValue, computersDeck)

makeDeck()
distinguishCard()
leftCardsNumber = len(deck)

printInfo()

attack('P',playersDeck)
