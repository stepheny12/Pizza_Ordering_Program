# functions go here
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")
# main routine code


want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes" or want_instructions == "y":
    print("In this program you would go through a process of steps to get the pizza you want ordered to you.")
    print("We would be getting your name, whether you'd like your pizza to be delivered or collect it from the store,")
    print("any extras etc...The maximum amount of pizzas you can order is 5 and at the end you'll have a chance of")
    print("winning a discount on your total price.")

print("program continues...")
print()
