menu = {
    'Pizza': 20,
    'Burger': 50,
    'Pasta': 30,
    'salad': 40,

}

print("Welcome to our resturant! Here's our menu:")
print('Pizza: Rs. 20\nBurger: Rs. 50\nPasta: Rs. 30\nSalad: Rs. 40')

order_total = 0

item_1 = input("Please enter the first item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your order for {item_1} has been added to the total. Current total: Rs. {order_total}")
else:
    print(f"sorry we don't have {item_1} on the menu.")


another_order = input("Do you want to order another item? (yes/no): ")
if another_order.lower() == 'yes':
    item_2 = input("Please enter the second item you want to order: ")
    if item_2 in menu:
        order_total += menu[item_2] 
        print( f"Your order for {item_2} has been added to the total. Current total: Rs. {order_total}")
    else:
        print(f"sorry we don't have {item_2} on the menu.")           