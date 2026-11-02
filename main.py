#imports and functions
from player import Player
from cards import Deck

playing = True

print("Welcome to War!")
input("Press 'Enter' to advance the round.")

def get_card_count(player_1_deck, player_2_deck):
    player_1_card_count = len(player_1_deck.cards)
    player_2_card_count = len(player_2_deck.cards)
    print(f"Player 1 has {player_1_card_count} cards. Player 2 has {player_2_card_count} cards.")


#game loop
while playing:

    #creates player decks and shuffles them
    player_1_deck = Deck(full=True)
    player_1_deck.shuffle()
    player_2_deck = Deck(full=True)
    player_2_deck.shuffle()

        # I didn't realize it was 2 deck war and wrote this to split the deck and deal it --Isaac
    #create a fresh deck object and then splits it
    #game_deck = Deck(full = True)
    #game_deck.shuffle()
    #for i, card in enumerate(game_deck.cards):
        #if i % 2 == 0:
            #player_1_deck.add_cards([card])
        #else:
            #player_2_deck.add_cards([card])

    game_running = True

    #create player instances
    player_1 = Player("Player 1", player_1_deck)
    player_2 = Player("Player 2", player_2_deck)

    cards_in_play = []

    while game_running:

        player_1_card = player_1.player_turn()
        player_2_card = player_2.player_turn()

        if player_1_card is None:
            print("Player 2 wins!")
            break
        elif player_2_card is None:
            print("Player 1 wins!")
            break

        #gameplay messages
        print(f"Player 1 drew the {player_1_card.rank} of {player_1_card.suit}!")
        print(f"Player 2 drew the {player_2_card.rank} of {player_2_card.suit}!")

        #evaluates cards and adds winner's card to cards_in_play first, then adds cards_in_play to winner's deck
        if player_1_card.value > player_2_card.value:
            cards_in_play.append(player_1_card)
            cards_in_play.append(player_2_card)
            print("Player 1 wins the round!\n")
            player_1.add_won_cards(cards_in_play)
            get_card_count(player_1_deck, player_2_deck)
            cards_in_play.clear()
        elif player_2_card.value > player_1_card.value:
            cards_in_play.append(player_2_card)
            cards_in_play.append(player_1_card)
            print("Player 2 wins the round!\n")
            player_2.add_won_cards(cards_in_play)
            get_card_count(player_1_deck, player_2_deck)
            cards_in_play.clear()
        else:
            cards_in_play.append(player_1_card)
            cards_in_play.append(player_2_card)
            print("War!")
            # do not add cards to any player, tiebreaker determined on the next round

        # the user will have to hit enter to submit anything, and since we're not using the input,
        # it's probably not worth validating. So this just acts as a pause.
        user_input = input("")

    user_play_again = input("Press 'y' to play again, else press any key to quit.").strip()
    if not (user_play_again.lower() == "y"):
        print("Thanks for playing!")
        break
