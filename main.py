MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
total_money = f"${money}"
# resources["water"] = resources["water"] - 1
# print(resources["water"])
user_choice = input("What would you like? (Espresso, Latte, or Cappuccino)")


# def total (c, total-mon):
#     return total-mon = total-mon + c 

def total(c, t = 0):
    return t + c





# if user_choice == "report":
#     print(resources["water"])
#     print(resources["milk"] )
#     print(resources["coffee"] ) 
#     print(total_money)
if user_choice == "Espresso":
    print("Cost is: 1.5")
    cost = 1.5
    print("Please insert coints")
    num_quarters = int(input("How many quarters?"))
    num_dimes = int(input("How many dimes?"))
    num_nickels = int(input("How many nickels?"))
    num_pennies = int(input("How many pennies?"))
    quarters = num_quarters * .25
    dimes = num_dimes * .10
    nickels = num_nickels * .05
    pennies = num_pennies * .01
    total_paid = quarters + dimes + nickels + pennies 
    if total_paid < cost:
        print("Sorry that is not enough money. Your payment is refunded")
    elif total_paid == cost:
        print("You paid the exact amount! Thank you!")
        # total_money += cost #Have to get this to work
        total_money = total(total_money, cost)
        resources["water"] = resources["water"] - 50 #Report isnt updating the inventory
        resources["coffee"] = resources["coffee"] - 18
    else:
        change = total_paid - cost
        print(f"Thanks for your purchase! Here is your change: {change}")
        resources["water"] = resources["water"] - 50 #Report isnt updating the inventory
        resources["coffee"] = resources["coffee"] - 18
        # total_money += cost #Have to get this to work
        total_money = total(total_money, cost)
elif user_choice == "report":
    print(resources["water"])
    print(resources["milk"] )
    print(resources["coffee"] ) 
    print(total_money)








