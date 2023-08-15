import pandas


# functions go here
# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine starts here
# set maximum number of tickets below
MAX_PIZZAS = 5

# dictionaries to hold ticket details
all_pizza = ["Pepperoni", "Hawaiian", "Cheesy Garlic", "MeatLover", "Beef & Onion", ]
all_pizza_costs = [8, 6, 6, 9, 8.5]


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
