import pandas


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


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


def pizza_choice(question):

    while True:
        response = input(question).lower()

        if response == "1":
            return "Pepperoni"

        if response == "2":
            return "Hawaiian"

        if response == "3":
            return "Cheesy Garlic"

        if response == "4":
            return "Meat Lover"

        if response == "5":
            return "Beef & Onion"

        if response == "6":
            return "Chicken Deluxe"

        if response == "7":
            return "Italian Lover"

        if response == "8":
            return "Margherita"

        if response == "9":
            return "Garlic Shrimp Deluxe"

        if response == "10":
            return "Mega Meat Lover"

        if response == "xxx":
            return "xxx"

        else:
            print("Please choose a valid pizza")


# gets what topping the user wants
def topping_choice(question):

    while True:
        response = input(question).lower()

        if response == "1":
            return "Pepperoni"

        if response == "2":
            return "Mushroom"

        if response == "3":
            return "Extra Cheese"

        if response == "4":
            return "Sausage"

        if response == "5":
            return "Olives"

        if response == "xxx":
            return "None"

        else:
            print("Please choose a valid topping")


# calculates the price of the pizza
def price_calc(var_pizza):
    if var_pizza == "Pepperoni":
        price = 8
    elif var_pizza == "Hawaiian":
        price = 6
    elif var_pizza == "Cheesy Garlic":
        price = 6
    elif var_pizza == "Meat Lover":
        price = 9
    elif var_pizza == "Beef & Onion":
        price = 8.5
    elif var_pizza == "Chicken Deluxe":
        price = 16.5
    elif var_pizza == "Italian Lover":
        price = 15
    elif var_pizza == "Margherita":
        price = 14
    elif var_pizza == "Garlic Shrimp Deluxe":
        price = 19
    elif var_pizza == "Mega Meat Lover":
        price = 20
    else:
        price = 0   # value for invalid pizza choices
    return price


# calculates the price of the topping
def topping_price_calc(var_topping):
    if var_topping == "Pepperoni":
        price = 1.5
    elif var_topping == "Mushroom":
        price = 1
    elif var_topping == "Extra Cheese":
        price = 1
    elif var_topping == "Sausage":
        price = 2
    elif var_topping == "Olives":
        price = 1
    else:
        price = 0   # value for invalid topping choices or none
    return price


# main routine starts here
# set maximum number of tickets below
MAX_PIZZAS = 5

# dictionaries to hold ticket details
all_pizza = ["1.Pepperoni", "2.Hawaiian", "3.Cheesy Garlic", "4.Meat Lover", "5.Beef & Onion",
             "6.Chicken Deluxe", "7.Italian Lover", "8.Margherita", "9.Garlic Shrimp Deluxe", "10.Mega Meat Lover"]
all_pizza_costs = [8, 6, 6, 9, 8.5, 16.5, 15, 14, 19, 20]
all_toppings = ["1.Pepperoni", "2.Mushrooms", "3.Extra Cheese", "4.Sausage", "5.Olives"]
all_topping_costs = [1.5, 1, 1, 2, 1]

pizza_program_dict = {
    "Pizza:": all_pizza,
    "Price": all_pizza_costs,
}
toppings_dict = {
    "Topping:": all_toppings,
    "Price": all_topping_costs,
}
pizza_program_frame = pandas.DataFrame(pizza_program_dict)
pizza_program_frame = pizza_program_frame.set_index('Pizza:')

pizza_program_frame['Price'] = pizza_program_frame['Price'].apply(currency)

topping_frame = pandas.DataFrame(toppings_dict)
topping_frame = topping_frame.set_index('Topping:')

topping_frame['Price'] = topping_frame['Price'].apply(currency)

# loop to sell tickets
pizzas_sold = 0
total_cost = 0
while pizzas_sold < MAX_PIZZAS:
    print("---- Pizza Menu ----")
    print()

    # output table with ticket data
    print(pizza_program_frame)
    print()
    pizza = pizza_choice("Please enter the corresponding number to the pizza you want or 'xxx' to quit: ")
    pizza_cost = price_calc(pizza)
    total_cost += pizza_cost  # Add the pizza cost to the total
    if pizza == 'xxx':
        print("You chose {}".format(pizza))
        break
    else:
        print("You chose {}, Pizza Price: ${:.2f}".format(pizza, pizza_cost))

    pizzas_sold += 1
    # get if they want toppings on the pizza
    topping = yes_no("Would you like to add any toppings to this pizza?")
    if topping == "yes":
        print("---- Topping Menu ----")
        print()
        # output table with topping data
        print(topping_frame)
        print()
        topping = topping_choice("Please enter the corresponding number to the topping you want or 'xxx' to quit: ")
        topping_cost = topping_price_calc(topping)
        cost = pizza_cost + topping_cost  # Add the topping cost to the pizza cost
        total_cost += topping_cost  # Add the topping cost to the total
        print()
        print("You chose {}, Pizza price with topping: ${:.2f}".format(topping, cost))
        print()
    if topping == "no":
        topping = "None"
        topping_cost = topping_price_calc(topping)
        cost = pizza_cost

# Output number of pizzas sold
if pizzas_sold == MAX_PIZZAS:
    print("Congratulations you have sold all the pizzas")
    print("The total price would be ${:.2f}".format(total_cost))

else:
    print("You have sold {} pizza/s. There is {} pizza/s "
          "remaining".format(pizzas_sold, MAX_PIZZAS - pizzas_sold))
    print("The total price would be ${:.2f}".format(total_cost))
