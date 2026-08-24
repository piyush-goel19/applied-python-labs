import random
from art import logo,vs
from game_data import data

def format_option(option):
    option = option["name"] + ", a " + option["description"] + ", from " + option["country"] + "."
    return option

def get_option(data):
    option = random.choice(data)
    return option

def get_winner(option1, option2):
    option1_followers = option1["follower_count"]
    option2_followers = option2["follower_count"]
    if option1_followers > option2_followers:
        return 'A'
    else:
        return 'B'

score = 0
first_option = ""
second_option = ""
end_game = False

while not end_game:
    print(logo)
    if score != 0:
        print(f"You're right! Current score: {score}.")

    if first_option == "":
        first_option = get_option(data)

    second_option = get_option(data)

    if first_option == second_option:
        second_option = get_option(data)

    print(f"Compare A: {format_option(first_option)}")

    print(vs)

    print(f"Against B: {format_option(second_option)}")

    winner = get_winner(first_option, second_option)
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_choice == winner:
        score += 1
        first_option = second_option
        print("\n" * 100)
    else:
        end_game = True
        print("\n" * 100)

print(logo)
print(f"Sorry, that's wrong. Final score: {score}")