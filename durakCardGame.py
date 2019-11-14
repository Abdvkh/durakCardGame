from random import shuffle, random

def makeDeck():
    global deck;
    global leftCardsNumber;
    deck = []
    suits = ['♠','♡','♢','♣']
    cards = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
             'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    for suit in suits:
        for card in cards:
            deck.append(suit+card)

    leftCardsNumber = len(deck)
    shuffle(deck)

def distinguishCard():
    global playersDeck
    global computersDeck

    playersDeck = [deck.pop() for i in range(6)]
    computersDeck = [deck.pop() for i in range(6)]

makeDeck()
distinguishCard()

print(deck,' ', leftCardsNumber, ' \n', playersDeck , ' | ', computersDeck, ' \n', deck, ' ', len(deck))
