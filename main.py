playing = True

print("Welcome to War!")
print("Press 'Enter' to advance the round.")

while playing:

    game_running = True
    # player_1 = player()
    # player_2 = player()

    cards_in_play = []

    while game_running:

        # player_1_card = player_1.draw_card()
        # player_2_card = player_2.draw_card()

        # cards_in_play.append(player_1_card)
        # cards_in_play.append(player_2_card)

        # if player_1_card.get_value() > player_2_card.get_value():
        #     print("Player 1 wins the round!")
            # add cards to Player 1's deck
        # elif player_2_card.get_value() > player_1_card.get_value():
        #     print("Player 2 wins the round!")
            # add cards to Player 2's deck
        # else:
        #     print("Tie!")
            # do not add cards to any player, tiebreaker determined on the next round

        # if player_1.deck_is_empty():
        #     print("Player 2 wins!")
        #     break
        # elif player_2.deck_is_empty():
        #     print("Player 1 wins!")
        #     break

        # the user will have to hit enter to submit anything, and since we're not using the input,
        # it's probably not worth validating. So this just acts as a pause.
        user_input = input("")

    user_play_again = input("Would you like to play again? [Y/n]")
    if not (user_play_again.lower() == "y" or len(user_play_again) == 0):
        print("Thanks for playing!")
        break
