import pandas


# functions go here
# sees if user inputs yes or no
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


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


# sees if user inputs wants delivery or collection
def delivery_collection(question):

    while True:
        response = input(question).lower()

        if response == "delivery" or response == "de":
            return "delivery"

        elif response == "collection" or response == "co":
            return "collection"

        else:
            print("Please choose a valid method")


def currency(x):
    return "${:.2f}".format(x)


def pizza_choice(question):

    while True:
        response = input(question).lower()

        if response == "pepperoni" or response == "pe":
            return "Pepperoni"

        if response == "hawaiian" or response == "ha":
            return "Hawaiian"

        if response == "cheesy garlic" or response == "che":
            return "Cheesy Garlic"

        if response == "meat lover" or response == "mea":
            return "Meat Lover"

        if response == "beef & onion" or response == "be":
            return "Beef & Onion"

        if response == "chicken deluxe" or response == "chi":
            return "Chicken Deluxe"

        if response == "italian Lover" or response == "ita":
            return "Italian Lover"

        if response == "margherita" or response == "mar":
            return "Margherita"

        if response == "garlic shrimp deluxe" or response == "gar":
            return "Garlic Shrimp Deluxe"

        if response == "mega meat lover" or response == "gar":
            return "Mega Meat Lover"

        else:
            print("Please choose a valid pizza")


# main routine code
# set maximum number of tickets below
MAX_PIZZAS = 5

# dictionaries to hold ticket details
all_pizza = ["Pepperoni", "Hawaiian", "Cheesy Garlic", "Meat Lover", "Beef & Onion", "Chicken Deluxe", "Italian Lover",
             "Margherita", "Garlic Shrimp Deluxe", "Mega Meat Lover"]
all_pizza_costs = [8, 6, 6, 9, 8.5, 16.5, 15, 14, 19, 20]

pizza_program_dict = {
    "Pizza:": all_pizza,
    "Price": all_pizza_costs,
}

pizza_program_frame = pandas.DataFrame(pizza_program_dict)
pizza_program_frame = pizza_program_frame.set_index('Pizza:')

pizza_program_frame['Price'] = pizza_program_frame['Price'].apply(currency)

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes" or want_instructions == "y":
    print("In this program you would go through a process of steps to get the pizza you want ordered to you.")
    print("We would be getting your name, whether you'd like your pizza to be delivered or collect it from the store,")
    print("any extras etc...The maximum amount of pizzas you can order is 5 and at the end you'll have a chance of")
    print("winning a discount on your total price.")

name = input("Please enter your name or 'xxx' to quit: ")

if name == 'xxx':
    print("Exiting program")

print("Welcome", name)

pizza_method = delivery_collection("Would you like it to be a delivery or collection from the store (delivery would "
                                   "have a surcharge of $5)?")

print("You chose", pizza_method)
print()

# loop to sell tickets
pizzas_sold = 0
while pizzas_sold < MAX_PIZZAS:
    print("---- Pizza Menu ----")
    print()

    # output table with ticket data
    print(pizza_program_frame)
    print()
    pizza = input("Please enter the pizza you want or 'xxx' to quit: ")
    print()
    if pizza == 'xxx':
        break

    pizzas_sold += 1


# Output number of pizzas sold
if pizzas_sold == MAX_PIZZAS:
    print("Congratulations you have sold all the pizzas")
else:
    print("You have sold {} pizza/s. There is {} pizza/s "
          "remaining".format(pizzas_sold, MAX_PIZZAS - pizzas_sold))

print("program continues...")
print()
