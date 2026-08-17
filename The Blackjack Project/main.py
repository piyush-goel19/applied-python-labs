import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_cards(no_of_cards_to_be_drawn, list_of_cards, score):
    for i in range(1, no_of_cards_to_be_drawn + 1):
        card_drawn = random.choice(cards)
        list_of_cards.append(card_drawn)
        score = score + card_drawn
    return score

def evaluate_score(u_score, c_score, won_by):
    if c_score > 21:
        print("Win, Opponent went over!")
        won_by = "User"
    elif u_score > 21:
        print("Lose, you went over!")
        won_by = "Computer"
    elif c_score == 21:
        print("Lose, opponent has Blackjack")
        won_by = "Computer"
    elif u_score == 21:
        print("Win, Blackjack!!")
        won_by = "User"

    return won_by

winner = ""

while input("Do you want to play a game of Blackjack? (y/n): ") == "y":
    print("\n"*50)
    print(art.logo)
    user_cards = []
    user_score = 0
    computer_score = 0
    computer_cards = []
    winner = ""
    user_score = draw_cards(2, user_cards, user_score)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    computer_score = draw_cards(1, computer_cards, computer_score)
    print(f"Computers/dealer's first card: {computer_cards}")
    winner = evaluate_score(user_score, computer_score, winner)
    while winner == "":
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_card == "n":
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            while computer_score <= 16 :
                computer_score = draw_cards(1, computer_cards, computer_score)
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            winner = evaluate_score(user_score, computer_score, winner)
            if winner != "":
                break
            if computer_score > user_score:
                winner = "Computer"
                print("You Lose!")
            elif user_score > computer_score:
                winner = "User"
                print("You Win!")
            else:
                winner = "None"
                print("Draw!")
        else:
            user_score = draw_cards(1, user_cards, user_score)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computers/dealer's first card: {computer_cards}")
            winner = evaluate_score(user_score, computer_score, winner)