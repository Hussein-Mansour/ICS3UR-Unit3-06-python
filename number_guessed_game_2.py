#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Thu/May5/2021
# This program is a Number Guessing Game


import random


def main():
    # this function checks if the number guessed is correct or wrong
    print("hey,guess the number if you can!\n")

    # input
    guessed_number_as_string = input("Enter the number between 0 - 9:")
    random_number = random.randint(1, 9)  # a number between 1 and 9

    # process & output
    try:
        guessed_number = int(guessed_number_as_string)

        if (guessed_number == random_number):
            print("\nYou guessed correct!")
        else:
            print("\nYou guessed wrong the number is {}!".format(random_number))
    except Exception:
        print("\n{} is not an integer!".format(guessed_number_as_string))
    finally:
        print("Thanks for playing.")

    print("\nDone.")


if __name__ == "__main__":
    main()
