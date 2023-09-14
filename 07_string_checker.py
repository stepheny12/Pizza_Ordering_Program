# checks that users enter a valid response (e.g. yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# main routine starts here
yes_no = ["yes", "no"]
method = ["collection", "delivery"]

for case in range(0, 5):
    want_instructions = string_checker("Do you want to read the "
                                       "instructions (y/n): ",
                                       1, yes_no)
    print("You chose", want_instructions)

for case in range(0, 5):
    pizza_method = string_checker("Would you like it to be a delivery or collection from the store? (de/co)",
                                  2, method)
    print("You chose", pizza_method)
