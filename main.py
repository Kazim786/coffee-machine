# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100
# }

# money = 0
# total_money = money #Might have to uncomment
# # resources["water"] = resources["water"] - 1
# # print(resources["water"])

# while True: 
#     user_choice = input("What would you like? (Espresso, Latte, or Cappuccino)")


# # def total (c, total-mon):
# #     return total-mon = total-mon + c 

# def total(c, t = 0):
#     t = float(t)
#     c = float(c)
#     return t + c





# # if user_choice == "report":
# #     print(resources["water"])
# #     print(resources["milk"] )
# #     print(resources["coffee"] ) 
# #     print(total_money)
# if user_choice == "Espresso":
#     print("Cost is: 1.5")
#     cost = 1.5
#     print("Please insert coints")
#     num_quarters = int(input("How many quarters?"))
#     num_dimes = int(input("How many dimes?"))
#     num_nickels = int(input("How many nickels?"))
#     num_pennies = int(input("How many pennies?"))
#     quarters = num_quarters * .25
#     dimes = num_dimes * .10
#     nickels = num_nickels * .05
#     pennies = num_pennies * .01
#     total_paid = quarters + dimes + nickels + pennies 
#     if total_paid < cost:
#         print("Sorry that is not enough money. Your payment is refunded")
#     elif total_paid == cost:
#         print("You paid the exact amount! Thank you!")
#         # global total_money
#         total_money += cost #Have to get this to work
#         # resources["total_money"] = total(resources["total_money"], cost)
#         #print(f"{resources['total_money']} test if cost payment is equal")
#         resources["water"] = resources["water"] - 50 #Report isnt updating the inventory
#         resources["coffee"] = resources["coffee"] - 18
#     else:
#         change = round(total_paid - cost)
#         print(f"Thanks for your purchase! Here is your change: {change}")
#         resources["water"] = resources["water"] - 50 #Report isnt updating the inventory
#         resources["coffee"] = resources["coffee"] - 18
#         # global total_money
#         total_money += cost #Have to get this to work
#         # resources['total_money'] = total(resources["total_money"], cost)
#         # print(resources["total_money"]) #So money is being updated to 1.5
# elif user_choice == "report":
#     print(resources["water"])
#     print(resources["milk"] )
#     print(resources["coffee"] ) 
#     print(total_money)




#Redoing the  work:

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


# print(MENU["espresso"]["ingredients"]["water"])
# print(MENU["espresso"]["cost"])


resources = {
    "water": 300, #300
    "milk": 200,
    "coffee": 100
}

# def adding ():
#     quarters = int(input("Please insert your quarters")) * .25 
#     dimes = int(input("Please insert your dimes")) * .10 
#     nickels = int(input("Please insert your nickels")) * .05 
#     pennies = int(input("Please insert your pennies")) * .01 
#     total_money = quarters + dimes + nickels + pennies 
#     return total_money

# money = adding



# print(MENU["espresso"]["cost"])

money = 0

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False 
    elif choice == "report":
        for items in resources:
            print(f" {items} : {resources[items]} \n Money: {money}")

#Time to check if resources are sufficient
    elif choice == "espresso":
        if resources["water"] < 50:
            print("There is not enough water")
        elif resources["coffee"] < 18:
            print("There is not enough Coffee")
        else:
            resources["water"] =   resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] =   resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]


    elif choice == "latte":
        if resources["water"] < 200:
            print("There is not enough water")
        elif resources["coffee"] < 24:
            print("There is not enough Coffee")
        elif resources["milk"] < 150:
            print("There is not enough Milk")
        else:

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
                if total_paid < MENU["latte"]["cost"]:
                    print("Your money is refunded. You dont have enough")
                elif total_paid == MENU["latte"]["cost"]:
                    print("You have no change, you paid exact amount!")
                    resources["water"] =   resources["water"] - MENU["latte"]["ingredients"]["water"]
                    resources["coffee"] =   resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                    resources["milk"] =   resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                    money+= MENU["latte"]["cost"]
                elif total_paid > MENU["latte"]["cost"]:
                    change = total_paid - MENU["latte"]["cost"]
                    print(f"Your change is: {change} ")
                    resources["water"] =   resources["water"] - MENU["latte"]["ingredients"]["water"]
                    resources["coffee"] =   resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                    resources["milk"] =   resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                    money += MENU["latte"]["cost"]

    elif choice == "cappuccino":
        if resources["water"] < 250:
            print("There is not enough water")
        elif resources["coffee"] < 24:
            print("There is not enough Coffee")
        elif resources["milk"] < 100:
            print("There is not enough Milk")
        else:
            resources["water"] =   resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] =   resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] =   resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]



#Resources is completed

#On number 5 now. This will have an if or elif statement
    

