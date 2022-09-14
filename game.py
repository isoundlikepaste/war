from classes import Player, Deck, Card



player_one = Player("one")
player_two = Player("two")

new_deck = Deck()
new_deck.shuffle()

#dealing all 52 cards amongst the two players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


# while game_on to check everytime if a player has lost
game_on = True
round_num = 0


while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.my_cards) == 0:
        print("Player One is out of cards!")
        game_on = False
        break
    if len(player_two.my_cards) == 0:
        print("Player Two is out of cards!")
        game_on = False
        break

    p1_play = []
    p1_play.append(player_one.remove_one())

    p2_play = []
    p2_play.append(player_two.remove_one())

    war_on = True
    while war_on:
        if p1_play[-1].value > p2_play[-1].value:
            player_one.add_cards(p1_play)
            player_one.add_cards(p2_play)
            break

        elif p1_play[-1].value < p2_play[-1].value:
            player_two.add_cards(p2_play)
            player_two.add_cards(p1_play)
            break

        elif p1_play[-1].value == p2_play[-1].value:
            print()
            print(f"WAR!! Player One now has {len(player_one.my_cards)} cards and Player 2 has {len(player_two.my_cards)} cards.")
            print()
            if len(player_one.my_cards) < 5:
                print("Player One doesnt have enough cards!")
                print("Player Two Wins!!")
                war_on = False
                game_on = False

            if len(player_two.my_cards) < 5:
                print("Player Two doesnt have enough cards!")
                print("Player One Wins!!")
                war_on = False
                game_on = False

            else:
                for t in range(5):
                    p1_play.append(player_one.remove_one())
                    p2_play.append(player_two.remove_one())

