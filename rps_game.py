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
"""


def get_hand(hand):
    rps_dict = {0: "scissor", 1: "rock", 2: "paper"}
    return rps_dict[hand]


def determine_winner(user_hand, computer_hand):
    pass


print("This application is a game of rock-paper-scissors.")
print("You will be playing against me. I will randomly choose.")
print("0 = scissor, 1 = rock, 2 = paper")
user_input = int(input("Please enter 0, 1, or 2: "))