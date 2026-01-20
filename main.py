from decks import Deck
from cards import Card

def main():
    testDeck = Deck()

    print(testDeck)
    print("")
    testDeck.deckShuffle()
    print(testDeck)
    print("")

    testCard1 = testDeck.draw()
    testCard2 = testDeck.draw()
    testCard3 = testDeck.draw()

    testCard4 = Card("Two", "Blue")

    print(testDeck.outPile)
    print("")

    testDeck.discard(testCard1)
    testDeck.discard(testCard2)
    testDeck.discard(testCard3)
    testDeck.discard(testCard4)

    print(testDeck.outPile)
    print("")
    print(testDeck.discardPile)


if __name__ == "__main__":
    main()