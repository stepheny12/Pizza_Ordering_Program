# functions go here
def delivery_collection(question):

    while True:
        response = input(question).lower()

        if response == "delivery" or response == "de":
            return "delivery"

        elif response == "collection" or response == "co":
            return "collection"

        else:
            print("Please choose a valid method")

# main routine code


while True:
    pizza_method = delivery_collection("Would you like it to be a delivery or collection from the store?")

    print("You chose", pizza_method)

    print("program continues")
