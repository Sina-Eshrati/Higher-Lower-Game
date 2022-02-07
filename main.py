from art import logo
from art import vs
from game_data import data
from replit import clear
import random

current_score = 0
game_continue = True
print(logo)

def pick_user():
    user = random.choice(data)
    return user

user_a = pick_user()
user_b = pick_user()
if user_a == user_b:
    user_b = pick_user()

while game_continue:
    print(f"Compare A: {user_a['name']}, a {user_a['description']}, from {user_a['country']}")
    print(vs)
    print(f"Against B: {user_b['name']}, a {user_b['description']}, from {user_b['country']}")

    choice = (input("Who has more followers? Type 'A' or 'B': ")).lower()

    if choice == 'a':
        if user_a['follower_count'] > user_b['follower_count']:
            current_score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {current_score}")
            user_a = user_b
            user_b = pick_user()
        else:
            clear()
            print(logo)
            print(f"Sorry that was wrong! final score: {current_score}")
            game_continue = False
    else:
        if user_b['follower_count'] > user_a['follower_count']:
            current_score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {current_score}")
            user_a = user_b
            user_b = pick_user()
        else:
            clear()
            print(logo)
            print(f"Sorry that was wrong! final score: {current_score}")
            game_continue = False

