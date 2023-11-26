import random
from art import logo


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(my_score, comp_score):

    if my_score > 21 and comp_score > 21:
        return "BUSTED! You lose 😤"

    if my_score == comp_score:
        return "PUSH! It's a tie 🙃"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif my_score == 0:
        return "Win with a Blackjack 😎"
    elif my_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif my_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():

    print(logo)

    my_cards = []
    comp_cards = []
    game_over = False
    for _ in range(2):
        my_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not game_over:
        my_score = calculate_score(my_cards)
        comp_score = calculate_score(comp_cards)
        print(f"   Your cards: {my_cards}  current score: {my_score}")
        print(f"   Computer's first card: {comp_cards[0]}")

        if my_score == 0 or comp_score == 0 or my_score > 21:
            game_over = True
        else:
            user_should_deal = input(
                "Type 'hit' to get another card, type 'stand' to pass: ").lower()
            if user_should_deal == "hit":
                my_cards.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"   Your final hand: {my_cards}, final score: {my_score}")
    print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(my_score, comp_score))


while input("♥️♠️ Do you want to play a game of Blackjack? (yes, no) ♦️♣  "
            ).lower() == "yes":
    play_game()
print("Thank you !")
