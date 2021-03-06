"""
Rock-Paper-Scissors Game

Code a game of rock paper scissors.

## Instructions

* take in a number 0-2 from the user that represents their hand
* generate a random number 0-2 to use for the computer's hand
* call the function `get_hand` to get the string representation of the user's hand
* call the function `get_hand` to get the string representation of the computer's hand
* call the function `determine_winner` to figure out who won
* print out the player hand and computer hand
* print out the winner

## Some Tips

Creating a function that gets a "hand" based on a number.

The function should take in a number and return the string representation of the hand. E.g.:
    # 0 = scissor, 1 = rock, 2 = paper
    # for example if the variable hand is 0, it should return the string "scissor"
    # possible combo 0-1, 0-2, 1-2
    0:scissor-1:rock , 1:rock wins
    0:scissor-2:paper, 0:scissor wins
    1:rock-2:paper, 2:paper wins
"""
import random


def get_hand(hand):
    rps_dict = {0: "scissor", 1: "rock", 2: "paper"}
    return rps_dict[hand]


def determine_winner(user_hand, computer_hand):
    u = get_hand(user_hand)
    c = get_hand(computer_hand)
    winner = "No one"
    if u == "scissor":
        if c == "rock":
            winner = "Computer"
        elif c == "paper":
            winner = "You"
    elif u == "paper":
        if c == "rock":
            winner = "You"
        if c == "scissor":
            winner = "Computer"
    elif u == "rock":
        if c == "paper":
            winner = "Computer"
        elif c == "scissor":
            winner = "You"
    return winner


print("This application is a game of rock-paper-scissors.")
print("You will be playing against me. I will randomly choose.")
print("0 = scissor, 1 = rock, 2 = paper")
user_input = int(input("Please enter 0, 1, or 2: "))

if not 0 <= user_input <= 2:
    print("I guess you don\'t want to play with me.")
else:
    computer_input = random.randint(0, 2)
    print(f"You chose {get_hand(user_input)}")
    print(f"I chose {get_hand(computer_input)}")
    print(f"{determine_winner(user_input, computer_input)} win(s).")
