
# main routine starts here
# set maximum number of tickets below
MAX_PIZZAS = 5

# loop to sell tickets
pizzas_sold = 0
while pizzas_sold < MAX_PIZZAS:
    name = input("Please enter the pizza you want or 'xxx' to quit: ")

    if name == 'xxx' :
        break

    pizzas_sold += 1

# Output number of pizzas sold
if pizzas_sold == MAX_PIZZAS:
    print("Congratulations you have sold all the pizzas")
else:
    print("You have sold {} pizza/s. There is {} pizza/s "
          "remaining".format(pizzas_sold, MAX_PIZZAS - pizzas_sold))
