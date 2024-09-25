class BlackJameGame:
    def __init__(self,depth) -> None:
        self.depth = depth+1
        print(self.depth)
        self.recursive = BlackJameGame(self.depth)
    
def main():
    BlackJameGame(0)

main()
