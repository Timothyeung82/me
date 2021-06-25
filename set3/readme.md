TODO: Reflect on what you learned this week and what is still unclear.
This week was a rough one but a fun one 

learn how to use try/except properly
learn how to turn str into int, but still can access the str later down the code (exercise 3)
exercise 4, the binary search was fairly strightfoward once I learn how to do the guessing game
I had trouble cutting down the amount of guesses at the start, since there are time when the range and the correct answer is right next to each other
but by doing 
if guess_input + 1 == actual_number:
                print(f"re-adjusted guess = {guess_input+1}")
                correct_anwser = True
            elif guess_input - 1 == actual_number:
                print(f"re-adjusted guess = {guess_input-1}")
                correct_anwser = True

I was able to solve it without too much of a problem
