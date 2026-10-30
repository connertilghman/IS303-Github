from player import Player
from cards import Card, Deck

playing = True

print("Welcome to War!")
print("Press 'Enter' to advance the round.")

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

        print(f"Player 1 drew the {player_1_card.rank} of {player_1_card.suit}!")
        print(f"Player 2 drew the {player_2_card.rank} of {player_2_card.suit}!")

        #evaluates cards and adds winner's card to cards_in_play first, then adds cards_in_play to winner's deck
        if player_1_card.value > player_2_card.value:
            cards_in_play.append(player_1_card)
            cards_in_play.append(player_2_card)
            print("Player 1 wins the round!")
            player_1.add_won_cards(cards_in_play)
            cards_in_play.clear()
        elif player_2_card.value > player_1_card.value:
            cards_in_play.append(player_2_card)
            cards_in_play.append(player_1_card)
            print("Player 2 wins the round!")
            player_2.add_won_cards(cards_in_play)
            cards_in_play.clear()
        else:
            cards_in_play.append(player_1_card)
            cards_in_play.append(player_2_card)
            print("War!")
            # do not add cards to any player, tiebreaker determined on the next round

        # the user will have to hit enter to submit anything, and since we're not using the input,
        # it's probably not worth validating. So this just acts as a pause.
        user_input = input("")

    user_play_again = input("Would you like to play again? [Y/n]").strip()
    if not (user_play_again.lower() == "y" or len(user_play_again) == 0):
        print("Thanks for playing!")
        break
