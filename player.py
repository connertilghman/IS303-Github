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


# I didn't realize it was 2 deck war and wrote this to split the deck and deal it --Isaac
#create a fresh deck object and then splits it
    #game_deck = Deck(full = True)
    #game_deck.shuffle()
    #for i, card in enumerate(game_deck.cards):
        #if i % 2 == 0:
            #player_1_deck.add_cards([card])
        #else:
            #player_2_deck.add_cards([card])