from cards import Card


def main():
    testCard1 = Card()
    testCard2 = Card("Two", "Clubs")
    testCard3 = Card("Ace", "Clubs")

    print(testCard1)
    
    print(testCard1 == testCard2)
    print(testCard1 == testCard3)
    print(testCard2 == 7)


if __name__ == "__main__":
    main()