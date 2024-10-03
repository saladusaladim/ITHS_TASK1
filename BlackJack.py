class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.score = 0
        # pass

    def __str__(self):
        return f"{self.name}."
    


