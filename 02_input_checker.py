# functions go here
# checks user enters a letter to given question
def chr_check(question):

    while True:

        response = input(question)
        if response.isdigit():
            print("Please enter an character.")
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# main routine goes here
while True:
    name = chr_check("Enter your name (or 'xxx' to quit) ")
    if name == "xxx":
        break

    print("Welcome {}".format(name))
