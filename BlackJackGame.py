import random

class Dealer:
    def __init__(self) -> None:
        self.hand = Hand()


    def draw(self,card):
            self.hand.addCard(card)
            

class Player:
    def __init__(self,name) -> None:
        self.hand = Hand()
        self.name = name

    def draw(self,card):
        self.hand.addCard(card)
        print(f'You drew {str(card)}, value of hand is {self.hand.getHandValue()}')

    def __str__(self) -> str:
        return(self.name)

class Deck:
    def __init__(self,shuffle=False) -> None:
        self.cards = self.generateCards()
        if shuffle:
            self.doShuffle()

    def generateCards(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks =  ['2', '3', '4', '5', '6', '7', '8','9','10','Jack','Queen','King','Ace']
        deck = []
        for suit in suits:
            for rank in ranks: 
                deck.append(Card(rank,suit))
        return(deck)
    
    def  doShuffle(self):
        random.shuffle(self.cards)

    def dealCard(self):
        if not self.cards:
            print ("No cards left in the deck")
            return    
        return(self.cards.pop(0))     

    def listCards(self):
        for card in self.cards:
            print(card)     
    
class Card:    
    def __init__(self,rank,suit) -> None:
        self.rank = rank
        self.suit = suit
        self.value = self.setValue()

    def getValue(self):
        return(int(self.value)) 
    

    def setValue(self):
        match self.rank:
            case 'Jack'|'Queen'|'King':
                value = 10
            case 'Ace':
                value = 1
            case _:
                value = int(self.rank)    
        return(value)

    def __str__(self) -> str:
        return f' < {self.rank} of {self.suit} with value {self.value} > '

class Hand: 
    def __init__(self) -> None:
        #self.value = 0
        self.cards = []

    def getHandValue(self):
        totalValue = 0
        if not self.cards:
            return(totalValue)     
        for card in self.cards:
            totalValue += card.getValue()        
        return (totalValue)
    
    def addCard(self,card):
        self.cards.append(card)

    def getCards(self):
        cardsInHand = ''
        if not self.cards:
            print('No cards in the hand')
            return cardsInHand        
        for card in self.cards:
            cardsInHand += f'{str(card)}'
        return(cardsInHand)