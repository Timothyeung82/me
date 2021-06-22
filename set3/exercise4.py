# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the world!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    tries = 0
    guess = 0

    correct_anwser = False
    
    while not correct_anwser:
        middle_number = (high + low) / 2
        remainder = middle_number - int(middle_number)
        if remainder > 0.5:
            middle_number = int(middle_number) + 1
        else:
            middle_number = int(middle_number)
        guess_input = middle_number
        if guess_input == actual_number:
            print(f"You got it!")
            tries += 1
            guess = actual_number
            print(f"tries = {tries}")
            print(f"guess = {guess}")
            correct_anwser = True
        elif guess_input < actual_number:
            guess = guess_input
            tries += 1
            print(f"tries = {tries}")
            print(f"guess = {guess}")
            if guess_input + 1 == actual_number:
                print(f"re-adjusted guess = {guess_input+1}")
                correct_anwser = True
            elif guess_input - 1 == actual_number:
                print(f"re-adjusted guess = {guess_input-1}")
                correct_anwser = True
            low = guess_input 
        elif guess_input > actual_number:
            guess = guess_input
            tries += 1
            print(f"tries = {tries}")
            print(f"guess = {guess}")
            if guess_input + 1 == actual_number:
                print(f"re-adjusted guess = {guess_input + 1}")
                correct_anwser = True
            elif guess_input - 1 == actual_number:
                print(f"re-adjusted guess = {guess_input -1 }")
                correct_anwser = True
            high = guess_input 

    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
