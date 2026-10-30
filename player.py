#player class
class Player():

    #created a fresh player with their half of the split, shuffled deck.
    def __init__(self, name, split_deck):
        self.name = name
        self.deck = split_deck

    #draws 1 card and returns it. If there are no cards left in the deck, returns None
    def player_turn(self):
        drawn_card = self.deck.draw()
        return drawn_card

    #adds the won cards back into the player's deck
    def add_won_cards(self, won_cards):
        self.deck.add_cards(won_cards)