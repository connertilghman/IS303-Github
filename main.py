from player import Player
from cards import Card, Deck

playing = True

print("Welcome to War!")
print("Press 'Enter' to advance the round.")

while playing:

    game_deck = Deck(full = True)
    game_deck.shuffle()

    player_1_deck = Deck(full=False)
    player_2_deck = Deck(full=False)

    #create a fresh deck object and then splits it
    for i, card in enumerate(game_deck.cards):
        if i % 2 == 0:
            player_1_deck.add_cards([card])
        else:
            player_2_deck.add_cards([card])

    game_running = True
    player_1 = Player("Player 1", player_1_deck)
    player_2 = Player("Player 2", player_2_deck)

    cards_in_play = []

    while game_running:

        player_1_card = player_1.player_turn()
        player_2_card = player_2.player_turn()

        if player_1_card == None:
            print("Player 2 wins!")
            break
        elif player_2_card == None:
            print("Player 1 wins!")
            break

        cards_in_play.append(player_1_card)
        cards_in_play.append(player_2_card)

        if player_1_card.value > player_2_card.value:
            print("Player 1 wins the round!")
            player_1.add_won_cards(cards_in_play)
        elif player_2_card.value > player_1_card.value:
            print("Player 2 wins the round!")
            player_2.add_won_cards(cards_in_play)
        else:
            print("War!")
            # do not add cards to any player, tiebreaker determined on the next round

        # the user will have to hit enter to submit anything, and since we're not using the input,
        # it's probably not worth validating. So this just acts as a pause.
        user_input = input("")

    user_play_again = input("Would you like to play again? [Y/n]")
    if not (user_play_again.lower() == "y" or len(user_play_again) == 0):
        print("Thanks for playing!")
        break
