"""Component 4 - game mechanics and looping v1
Based on 05_token_generator_v4but hard-wired to only allocate donkeys
Gives user feedback about number of rounds nd maintains balance.
Test amount set to $5
"""

import random

# Main routine
TEST_AMOUNT= 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

# Testing loop to generate 5 tokens
while play_again != "x":
    rounds_played += 1 #keep track of rounds
    number = random.randint(6, 36) # can only be a donkey

    # adjust balance
    # if the random number is between 1 and 5
    # user gets  unicorn (add $4 to balance)
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

    # if the random number is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1

    # in all other cases the token must be a horse or a zebra
    # (subtract $0.50 from the balance in either case)
    else:
        # if the number is even, set the token to zebra
        if number % 2 == 0:
            token = "zebra"
            balance -= .50

        # otherwise, set the token to horse
        else:
            token = "horse"
            balance -= .5

    # output
    print(f"Token: {token}, Balance: {balance:.2f}")
