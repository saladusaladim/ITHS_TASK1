from BlackJack import Player
# from BlackJack import Deck
import emojis


class BlackJameGame:
    def __init__(self) -> None:
        self.a = BlackJack.Player("Erik")
        # self.depth = depth+1
        # print(self.depth)
        # self.recursive = BlackJameGame1(self.depth)

    def GetName(self):
        return self.a.name
    
def main():
    print(':snake:')
    
    
    
    b = BlackJameGame()
    print(b.GetName())
  


main()
