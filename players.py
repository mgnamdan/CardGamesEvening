class BJPlayer:
    
    RANKVALUES = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
                  "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10,
                  "Queen": 10, "King": 10, "Ace": 11}


    def __init__(self, name="Player"):
        self.name = name
        self.reset()


    def __repr__(self):
        return f"{self.name}"


    def __eq__(self, other):
        if isinstance(other, BJPlayer):
            if self.name != other.name:
                return False
            if self.score != other.score:
                return False
            if len(self.hand) == len(other.hand):
                for cardIdx in range(len(self.hand)):
                    if self.hand[cardIdx] != other.hand[cardIdx]:
                        return False
            else:
                return False
            return True
        else:
            return False
        

    def reset(self):
        self.hand = []
        self.score = 0


    def showHand(self):
        for cardIdx in range(len(self.hand)):
            print(f"{cardIdx+1}. {self.hand[cardIdx]}")


    def giveScore(self):
        return self.score


    def drawCard(self, card):
        self.hand.append(card)


    def calcScore(self):
        self.score = 0
        for card in self.hand:
            self.score += self.RANKVALUES[card.rank]


    def makeChoice(self):
        self.calcScore()
        if self.score < 17:
            return "hit"
        else:
            return "stay"
        


class HumanBJPlayer(BJPlayer):
     
    def __init__(self, name="Player"):
        super().__init__(name)


    def __eq__(self, other):
        if isinstance(other, HumanBJPlayer):
            if self.name != other.name:
                return False
            if self.score != other.score:
                return False
            if len(self.hand) == len(other.hand):
                for cardIdx in range(len(self.hand)):
                    if self.hand[cardIdx] != other.hand[cardIdx]:
                        return False
            else:
                return False
            return True
        else:
            return False


    def makeChoice(self):
        validChoice = False
        while not validChoice:
            self.showHand()
            print("Would you like to hit or stay?")
            choice = input(" --> ").lower()
            if choice == "hit" or choice == "h":
                choice = "hit"
                validChoice = True
            elif choice == "stay" or choice == "s":
                choice = "stay"
                validChoice = True
            else:
                print("That's not an option! Try again!")
        return choice
    