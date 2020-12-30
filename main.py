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

user_choice = input("What would you like? (Espresso, Latte, or Cappuccino)")

if user_choice == "report":
    print(resources["water"])
    print(resources["milk"] )
    print(resources["coffee"] ) 
    print(total_money)



print("Please insert coints")

quarters = input("How many quarters?")
dimes = input("How many dimes?")
nickels = input("How many nickels?")
pennies = input("How many pennies?")



