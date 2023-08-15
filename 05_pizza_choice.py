import pandas


# functions go here
# currency formatting function
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


# main routine starts here
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

# loop to sell tickets
pizzas_sold = 0
while pizzas_sold < MAX_PIZZAS:
    print("---- Pizza Menu ----")
    print()

    # output table with ticket data
    print(pizza_program_frame)
    print()
    pizza = pizza_choice("Please enter the pizza you want or 'xxx' to quit: ")
    print("You chose", pizza)
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
