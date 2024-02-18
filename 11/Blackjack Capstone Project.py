############### Blackjack Project #####################
import random
from art import logo
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def generate_cards_user():
    return random.sample(cards,3)
def generate_cards_dealer():
    return random.sample(cards,2)
ask_user = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n ").lower()
if ask_user == "n":
    user_play = False
    print("Thanks for playing.")

def blackjack_game():
    user_play = True
    print(logo)
    user_cards = generate_cards_user()
    dealer_cards = generate_cards_dealer()

    while user_play == True:

        print(f"Your cards: [{user_cards[0]}" + f", {user_cards[1]}]")
        print(f"Computer's first card: {dealer_cards[0]}")
        another_card = input("Type 'y' to get another card, type 'n' to pass:\n ").lower()

        if another_card == "y":
            print(f"Your cards: [{user_cards[0]}" + f", {user_cards[1]}]")
            print(f"Computer's first card: {dealer_cards[0]}")
            total = 0
            com_total = 0
            for num in range(0,len(user_cards)):
                total = total + user_cards[num]
            for com_num in range(0, len(dealer_cards)):
                com_total = com_total + dealer_cards[com_num]

            if total > 21:
                print(f"Your final hand: {user_cards}, final score: {total}")
                print(f"Computer's final hand: {dealer_cards}, final score: {com_total} ")
                print("You went over. You lose.")

            elif com_total > 21:
                print(f"Your final hand: {user_cards}, final score: {total}")
                print(f"Computer's final hand: {dealer_cards}, final score: {com_total} ")
                print("Dealer went over. You win.")
            elif total > com_total & total <= 21:
                print(f"Your final hand: {user_cards}, final score: {total}")
                print(f"Computer's final hand: {dealer_cards}, final score: {com_total} ")
                print("You win")
            elif com_total > total & com_total <= 21:
                print(f"Your final hand: {user_cards}, final score: {total}")
                print(f"Computer's final hand: {dealer_cards}, final score: {com_total} ")
                print("You win")
            else:
                print(f"Your final hand: {user_cards}, final score: {total}")
                print(f"Computer's final hand: {dealer_cards}, final score: {com_total} ")
                print("It's a draw")


        else:
            total_user_hand = user_cards[0] + user_cards[1]
            total_computer_hand = dealer_cards[0] + dealer_cards[1]
            print(f"Your final hand: [{user_cards[0]}" + f", {user_cards[1]}]")
            print(f"Computer's final hand: {dealer_cards}")

            if total_user_hand > total_computer_hand:
                print("You win")
            elif total_computer_hand > total_user_hand:
                print("You lose")
            else:
                print("It's a draw")


        ask_user = input("Do you want to play another game of Blackjack? Type 'y' or 'n':\n ").lower()
        if ask_user == "y":
            blackjack_game()

        if ask_user == "n":
            print("Thanks for playing.")
            exit()


blackjack_game()