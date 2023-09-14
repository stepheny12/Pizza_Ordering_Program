import pandas
import random
from datetime import date


# functions go here

# checks user enters a letter to given question
def chr_check(question):

    while True:

        response = input(question)
        if response.isdigit():
            print("Please only enter characters")
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# sees if user inputs wants delivery or collection
def currency(x):
    return "${:.2f}".format(x)


# gets what pizza the user wants
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
def pizza_price_calc(var_pizza):
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


# checks that users enter a valid response (e.g. yes / no
# collection / delivery) based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# main routine code
yes_no = ["yes", "no"]
method = ["collection", "delivery"]

# set maximum number of pizzas below
MAX_PIZZAS = 5
# dictionaries to hold pizza details and ordering info
all_pizza = ["1.Pepperoni", "2.Hawaiian", "3.Cheesy Garlic", "4.Meat Lover", "5.Beef & Onion",
             "6.Chicken Deluxe", "7.Italian Lover", "8.Margherita", "9.Garlic Shrimp Deluxe", "10.Mega Meat Lover"]
all_pizza_costs = [8, 6, 6, 9, 8.5, 16.5, 15, 14, 19, 20]
all_toppings = ["1.Pepperoni", "2.Mushrooms", "3.Extra Cheese", "4.Sausage", "5.Olives"]
all_topping_costs = [1.5, 1, 1, 2, 1]
all_order_pizzas = []
all_order_pizzas_costs = []
all_order_toppings = []
all_order_toppings_costs = []
all_order_totals = []

pizza_program_dict = {
    "Pizza:": all_pizza,
    "Price": all_pizza_costs,
}
toppings_dict = {
    "Topping:": all_toppings,
    "Price": all_topping_costs,
}
order_dict = {
    "Order:": all_order_pizzas,
    "Pizza Price:": all_order_pizzas_costs,
    "Topping:": all_order_toppings,
    "Topping Price:": all_order_toppings_costs,
    "Total:": all_order_totals
}
pizza_program_frame = pandas.DataFrame(pizza_program_dict)
pizza_program_frame = pizza_program_frame.set_index('Pizza:')

pizza_program_frame['Price'] = pizza_program_frame['Price'].apply(currency)

topping_frame = pandas.DataFrame(toppings_dict)
topping_frame = topping_frame.set_index('Topping:')

topping_frame['Price'] = topping_frame['Price'].apply(currency)

# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")
date = "Date {}/{}/{}".format(day, month, year)

# introduction
print("Welcome to Papas Pizzerias Pizza ordering Program ")
want_instructions = string_checker("Do you want to read the instructions (y/n)? ", 1, yes_no)

# output instructions is they want it
if want_instructions == "yes" or want_instructions == "y":
    print('''
    ---------------Instructions-----------------
    Welcome to Papas Pizzerias Online Ordering Program.
    For your order you would have to go through these steps:
    -Enter user name (can't be blank and can't be a number)
    -Enter what method for your pizza order (collection/delivery)
    -Enter the corresponding number to the pizza you want that's shown on the menu
    -If you want a topping, enter the corresponding number to the topping you want
    
    During this process you may order up to 5 pizzas and each pizza can only have 1 topping. 
    If you want to exit the program or you've ordered enough pizzas type 'xxx' to quit
    
    The program would display your order details such as the pizzas you've ordered, their price,
    if the pizza has any toppings, the toppings price and the total for each pizza.
    
    At the end of the program you would have a chance to win a 10% discount on your order as well!
    Any purchases made during this program would be via online transactions.
    We hope you enjoy our online Pizza Ordering program and tell all your peers about it.
    
    ------------------------------------------------''')
# get name
name = chr_check("Please enter your name or 'xxx' to quit: ")

if name == 'xxx':
    print("Exiting program")

# delivery info variables
phone = ""
address = ""

# ordering pizza loop
while True:
    print()
    print("Welcome", name)

    pizza_method = string_checker("Would you like it to be a delivery or collection from the store (de/co)"
                                  " (delivery would have a surcharge of $7.5)?", 2, method)
    print("You chose", pizza_method)

    if pizza_method == 'delivery':
        print("Please enter your delivery info:")
        phone = input("Phone Number:")
        address = input("Address:")
        print()
        print("Deliver info:")
        print("Phone number:", phone)
        print("Address:", address)

    print()

    # loop to sell pizza
    pizzas_sold = 0
    total_cost = 0
    if pizza_method == 'delivery':
        total_cost += 7.50

    while pizzas_sold < MAX_PIZZAS:
        print("---- Pizza Menu ----")
        print()

        # output table with pizza data
        print(pizza_program_frame)
        print()
        pizza = pizza_choice("Please enter the corresponding number to the pizza you want or 'xxx' to quit: ")
        pizza_cost = pizza_price_calc(pizza)
        total_cost += pizza_cost  # Add the pizza cost to the total
        if pizza == 'xxx':
            print("You chose to quit}")
            break
        else:
            print("You chose {}, Pizza Price: ${:.2f}".format(pizza, pizza_cost))

        pizzas_sold += 1
        # get if they want toppings on the pizza
        topping = string_checker("Would you like to add any toppings to this pizza?", 1, yes_no)
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
            # Update the order_dict with order information
            order_dict["Order:"].append(pizza)  # Add pizza name
            order_dict["Pizza Price:"].append(pizza_cost)  # Add pizza price
            order_dict["Topping:"].append(topping)  # Add topping name
            order_dict["Topping Price:"].append(topping_cost)  # Add topping price
            order_dict["Total:"].append(cost)  # Add total cost
        # make topping none if they don't want it
        if topping == "no":
            topping = "None"
            topping_cost = topping_price_calc(topping)
            cost = pizza_cost

            # Update the order_dict with order information
            order_dict["Order:"].append(pizza)  # Add pizza name
            order_dict["Pizza Price:"].append(pizza_cost)  # Add pizza price
            order_dict["Topping:"].append(topping)  # Add topping name
            order_dict["Topping Price:"].append(topping_cost)  # Add topping price
            order_dict["Total:"].append(cost)  # Add total cost

    # Create the Order frame
    order_frame = pandas.DataFrame(order_dict)
    order_frame["Pizza Price:"] = order_frame["Pizza Price:"].apply(currency)
    order_frame["Topping Price:"] = order_frame["Topping Price:"].apply(currency)
    order_frame["Total:"] = order_frame["Total:"].apply(currency)

    # Output number of pizzas sold
    if pizzas_sold == MAX_PIZZAS:
        print("Congratulations you have sold all the pizzas")
        print()
        print("Here is your order:")
        print("**************************************************")
        print()
        print(order_frame.to_string(index=False, justify="left", col_space=15))
        print()
        print("**************************************************")
        print()
        print("The total price would be ${:.2f}".format(total_cost))

    else:
        print("You have sold {} pizza/s. There is {} pizza/s "
              "remaining".format(pizzas_sold, MAX_PIZZAS - pizzas_sold))
        print()
        print("Here is your order:")
        print("**************************************************")
        print()
        print(order_frame.to_string(index=False, justify="left", col_space=15))
        print()
        print("**************************************************")
        print()
        print("The total price would be ${:.2f}".format(total_cost))

    # get confirmation if user wants to confirm their order or restart
    confirmation = string_checker("Are you sure you want to process this order (y/n)", 1, yes_no)
    if confirmation == "yes":
        # customer has a 25% chance to win a 10% discount
        discount = random.randint(1, 4)
        if discount == 2:
            total_cost = total_cost * 0.9
            print("Congratulations you have won a 10% discount for your order!")
        else:
            print("Unfortunately you didn't win any discounts")
        print("Here's your final receipt:")
        print("----------Receipt----------")
        print(date)
        print(name)
        print()
        if pizza_method == 'delivery':
            print("Deliver info:")
            print("Phone number:", phone)
            print("Address:", address)
            print()
        print(order_frame.to_string(index=False, justify="left", col_space=15))
        print()
        if pizza_method == 'delivery':
            print("Delivery fees: $7.50")
        print("The total cost would be ${:.2f}".format(total_cost))

        print()

        break
    # if confirmation no then go on to if they want to reorder
    if confirmation == "no":
        reorder = string_checker("Would you like to go through the ordering process again?", 1,
                                 yes_no)
        # clears the information they input if they choose yes, so they can start again
        if confirmation == "yes":
            all_order_pizzas = []
            all_order_pizzas_costs = []
            all_order_toppings = []
            all_order_toppings_costs = []
            all_order_totals = []
            pizzas_sold = 0
            total_cost = 0
        # go out of loop if no
        if reorder == "no":
            break

print()
print("Thanks for using Papas Pizzeria Pizza Program")
# program ends
print("Program ends")
