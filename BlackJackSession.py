from BlackJackGame import Player
from BlackJackGame import Card
from BlackJackGame import Deck
from BlackJackGame import Hand
from BlackJackGame import Dealer


def main():
    dealer = Dealer()
    print('Welcome to Black Jack, please enter your name:')
    player = Player(input())
    print(f'Hello {str(player)}, the game will now start.')
    print('Setting up deck and dealing the first cards...')
    deck = Deck(shuffle=True)

    dealer.draw(deck.dealCard())
    dealer.draw(deck.dealCard())
    
    player.draw(deck.dealCard())
    player.draw(deck.dealCard())


    print(f'Dealers visible card: {dealer.hand.cards[0]}')

    while True:
        print('Do you want to hit or stand? Type the word:')
        action = input()
        if action.lower() == 'hit':
            player.draw(deck.dealCard())
            print(f'Your hand: {player.hand.getCards()}')
            if player.hand.getHandValue() > 21:
                print('You busted! Dealer wins.')
                break
        elif action.lower() == 'stand':
            break
        else:
            print('Invalid action. Please try again.')

    if player.hand.getHandValue() <= 21:
        while dealer.hand.getHandValue() < 17:
            dealer.draw(deck.dealCard())
        print(f'Dealers hand: {dealer.hand.getCards()}')
        if dealer.hand.getHandValue() > 21:
            print('Dealer busted! You win!')
        elif dealer.hand.getHandValue() < player.hand.getHandValue():
            print('You win!')
        elif dealer.hand.getHandValue() > player.hand.getHandValue():
            print('Dealer wins.')
        else:
            print('Its a tie!')


main()







    

