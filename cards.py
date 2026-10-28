# Information about the cards in a standard deck of playing cards
import random
 
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King", "Ace"]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = ranks.index(rank) + 2

class Deck:
    def __init__(self, full=True):
        #creates a deck of cards, if full is True, creates a full deck of 52 cards, otherwise creates an empty deck
        cards = []
        if full:
            for s in suits:
                for r in ranks:
                    cards.append(Card(r, s))
        self.cards = cards
 
    def shuffle(self):
        random.shuffle(self.cards)
 
    def draw(self):
        #takes first card from the deck and returns it, if there are no cards left, returns None
        if self.cards:
            return self.cards.pop(0)
        else:
            return None

    def add_cards(self, cards):
        self.cards.extend(cards)