from random import shuffle, choice

global leftCardsNumber

def printInfo():
    '''Prints all the avaliable info'''

    print(f"*Deck: {deck}\n\n*Left cards number: {leftCardsNumber}\n\n*Trump is {trump} \n\n*Player's deck: {playersDeck}\n\n*Computer's deck: {computersDeck}")

def playground(part, partsCard):#,isNotPlayground):
    '''Game\'s playground'''

   # if isNotPlayground:
    #  print('This is the playground: \n\n')
     # isNotPlayground = False

    print(part, ":", partsCard)

    
    
#first 
def makeDeck():
    '''Creates and shuffles the deck and declares the trump'''

    global deck;
    global trump;

    deck = []
    suits = ['♠','♡','♢','♣']
    cards = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
             'J': 11, 'Q': 12, 'K': 13, 'A': 14}
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
    
    index = int(input(f"Please choose the card you want to attack, just send the number from 0 till {partsDeckLength}\n>"))

    chosenCard = partsDeck[index]
    playground(part,chosenCard)




makeDeck()
distinguishCard()
leftCardsNumber = len(deck)

printInfo()

attack('P',playersDeck)
