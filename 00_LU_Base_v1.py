"""LU Base Component
Components dded after thy have created and tested"""


# yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Instructions'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


# function to display instructions
def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game will go here")
    print()
    print("Program continues")
    print()


# number checking function
def num_check(question, low, high):
    error = "That was not valid input\n" \
            "PLease enter a number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount (1-10) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check or number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine go here...
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()
else:
    print("Program continues")


# ask the user how much the want to play with
user_balance= num_check("How much would you like to pay with? $", 1, 10)
print(f"You are playing with ${user_balance}")