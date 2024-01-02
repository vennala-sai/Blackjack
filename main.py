
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import art
import random


def blackjack():
    print(art.logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def random_card():
        return random.randint(0, len(cards) - 1)

    user_cards = [cards[random_card()], cards[random_card()]]
    computer_cards = [cards[random_card()], cards[random_card()]]
    should_continue = True
    while should_continue:
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            should_continue = True
            user_cards.append(cards[random_card()])
            if sum(user_cards) > 21:
                break
            if (sum(computer_cards) < 21):
                computer_cards.append(cards[random_card()])
        else:
            should_continue = False

    print(f"Your final hand:{user_cards}, final score: {sum(user_cards)}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}"
    )
    if sum(user_cards) > sum(computer_cards) and sum(user_cards) <= 21:
        print("You win!")
    elif sum(user_cards) == sum(computer_cards):
        print("You draw!")
    else:
        print("You lose!")
    if input("Do you want to play Blackjack again? 'y' or 'n': ") == 'y':
        blackjack()


if input("Do you want to play Blackjack? 'y' or 'n': ") == 'y':
    blackjack()

