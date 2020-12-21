food_name     ="salad"# string
food_price    =50.00  # float
food_available=10     # int



# calculations

client_quantity=int(input("How many?"))

if client_quantity > 0 and client_quantity<=food_available :
    food_total_cost = food_price * client_quantity
# output
    print("TOTAL:", food_total_cost)
else:
    print("Sorry, quantity is not available")
