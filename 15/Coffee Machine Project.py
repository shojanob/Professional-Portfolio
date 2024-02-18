menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

total_money = 0

def report(user_money = 0):
    for resource in resources:
        if resource == "water" or "milk" or resource == "coffee":
            add_units = "ml" if resource in ["water", "milk"] else "g"
            amount = resources[resource]
            print(f"{resource.title()}: {amount}{add_units}")
    add_dollar_sign = "$"
    amount_money = add_dollar_sign + str(user_money)
    print(f"Money: {amount_money}")

# TODO 1 Prompt user by asking "What would you like? (espresso/latte/cappuccino)”
# TODO 2 Print report of resource values


drink_choice = ""

while drink_choice != "off":
    drink_choice = input("What would you like? (espresso/latte/cappuccino)\n").lower()
    if drink_choice in ["espresso", "latte", "cappuccino"]:
        if resources["water"] >= menu[drink_choice]["ingredients"]["water"] and \
                resources["milk"] >= menu[drink_choice]["ingredients"]["milk"] and \
                resources["coffee"] >= menu[drink_choice]["ingredients"]["coffee"]:
            for drink in menu:
                if drink_choice == drink:
                    for drink_ingredient in menu[drink_choice]["ingredients"]:
                        resources[drink_ingredient] -= menu[drink_choice]["ingredients"][drink_ingredient]

                    user_money = menu[drink_choice]["cost"]


                    print("Please insert coins")
                    user_quarters = int(input("How many quarters?: "))
                    user_dimes = int(input("How many dimes?: "))
                    user_nickles = int(input("How many nickles? "))
                    user_pennies = int(input("How many pennies? "))

                    quarters = 0.25 * user_quarters
                    dimes = 0.10 * user_dimes
                    nickles = 0.05 * user_nickles
                    pennies = 0.01 * user_pennies
                    money_total = quarters + dimes + nickles + pennies


                    if money_total >= user_money:
                        change = money_total - user_money
                        if change > 0:
                            print(f"Here is your change: ${change:.2f}")

                        print(f"Here is your {drink_choice}. Enjoy!")
                        total_money += user_money
                    elif money_total < user_money:
                        print("Sorry that's not enough money. Money refunded.")
                    else:
                        print("Transaction successful")
                        print(f"Here is your {drink_choice}. Enjoy!")
                        total_money += user_money
                    break
        else:
            print(f"Sorry there are not enough resources to make {drink_choice}")
    elif drink_choice == "off":
        exit()
    elif drink_choice == "report":
        report(total_money)