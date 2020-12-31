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
    "coffee": 100
}

money = 0
total_money = money #Might have to uncomment
# resources["water"] = resources["water"] - 1
# print(resources["water"])

while True: 
    user_choice = input("What would you like? (Espresso, Latte, or Cappuccino)")


# def total (c, total-mon):
#     return total-mon = total-mon + c 

def total(c, t = 0):
    t = float(t)
    c = float(c)
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
        # global total_money
        total_money += cost #Have to get this to work
        # resources["total_money"] = total(resources["total_money"], cost)
        #print(f"{resources['total_money']} test if cost payment is equal")
        resources["water"] = resources["water"] - 50 #Report isnt updating the inventory
        resources["coffee"] = resources["coffee"] - 18
    else:
        change = round(total_paid - cost)
        print(f"Thanks for your purchase! Here is your change: {change}")
        resources["water"] = resources["water"] - 50 #Report isnt updating the inventory
        resources["coffee"] = resources["coffee"] - 18
        # global total_money
        total_money += cost #Have to get this to work
        # resources['total_money'] = total(resources["total_money"], cost)
        # print(resources["total_money"]) #So money is being updated to 1.5
elif user_choice == "report":
    print(resources["water"])
    print(resources["milk"] )
    print(resources["coffee"] ) 
    print(total_money)








