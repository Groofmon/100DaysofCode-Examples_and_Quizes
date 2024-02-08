from random import choice
cards_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards_value = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}
player_value, com_value = 0, 0
player_deck, com_deck = [], []
player_deck_A, com_deck_A = [], []

# is_end = False
is_stay = False
player_won = False
com_won = False
is_com_turn = True


def hit_player():
    global player_value
    global player_deck_A
    global player_deck

    drawn_card = choice(cards_list)
    player_deck.append(drawn_card)

    if drawn_card == "A":
        player_value += 11
        player_deck_A.append(drawn_card)

    # elif drawn_card == "A" and player_value > 10:
    #     player_value += 1
    else:
        player_value += cards_value[drawn_card]


def hit_com():
    global com_value
    global com_deck_A
    global com_deck

    drawn_card = choice(cards_list)
    com_deck.append(drawn_card)

    if drawn_card == "A":
        com_value += 11
        com_deck_A.append(drawn_card)

    # elif drawn_card == "A" and player_value > 10:
    #     player_value += 1
    else:
        com_value += cards_value[drawn_card]


# -----------------------------------------
print("Welcome to BlackJack 21!")
input("Press Enter to begin!")
# Initialize
hit_player()
hit_com()

while True:
    # Player Turn
    hit_player()

    print(30 * "=")
    print(f"Your Deck: {str(player_deck)} equal to {player_value}")
    print(f"Com deck:  [{[com_deck[0]]},[X]]")
    print(30 * "=")

    # Pre value check
    if player_value > 21 and "A" in player_deck_A:
        player_deck_A.pop()
        player_value -= 10
    elif player_value > 21:
        print("Busted! You lose!")
        exit()
    elif player_value == 21:
        print("Blackjack! You Win!")
        exit()

    player_next_move = input("stay or hit : ")
    if player_next_move == "stay":
        break

while player_value < 21 and com_value < 17:
    # Computer Turn
    hit_com()

    print(30 * "=")
    print(f"Your Deck: {str(player_deck)} equal to {player_value}")
    print(f"Com deck:  {str(com_deck)} equal to {com_value}")
    print(30 * "=")

    if com_value > 21 and "A" in com_deck_A:
        com_deck_A.pop()
        com_value -= 10
    elif com_value > 21:
        print("Dealer Busted, You win!")
        exit()
    elif com_value == 21 and player_value != 21:
        print("Dealer had Blackjack! You lose!")
        exit()

if player_value > com_value:
    print("Your win!")
elif com_value > player_value:
    print("You lose!")
elif player_value == com_value:
    print("Draw!")
