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


def get_report():
    """Outputs the resource levels"""
    for resource in resources:
        if resource == "coffee":
            print(f"{resource.title()}: {resources[resource]}g")
        else:
            print(f"{resource.title()}: {resources[resource]}ml")


# TODO: 4. Check if the resources are sufficient for user's order.
def check_resource_levels(user_selection):
    # TODO: 4b. If any resources are insufficient for that particular drink, print "Sorry there is not enough {resource}.
    # TODO: 5a. If there are sufficient resources to make the selected drink, prompt the user to insert coins.
    if MENU[user_selection]["ingredients"]["water"] > resources["water"]:
        low_item = "water"
        print(f"Sorry, there is not enough {low_item}.")
    elif MENU[user_selection]["ingredients"]["milk"] > resources["milk"]:
        low_item = "milk"
        print(f"Sorry, there is not enough {low_item}.")
    elif MENU[user_selection]["ingredients"]["coffee"] > resources["coffee"] < 24:
        low_item = "coffee"
        print(f"Sorry, there is not enough {low_item}.")
    else:
        print(f"Please insert coins")


# Variable to keep track of the profit generated.
sales_profit = 0

# TODO: 1. Ask user what they would like? (espresso/latte/cappuccino/off/report).
powered_on = True
# TODO: 1b. The prompt should show every time an action has been completed. eg) Once the drink has dispensed.
while powered_on:
    # TODO: 1a. Check the user's input to decide what to do next.
    choice = input(" What would you like? (espresso: $1.50/latte: $2.50/cappuccino $3.00: ").lower()
    # TODO: 2. Turn the coffee machine off by entering 'off' in the prompt.
    if choice == 'off':
        break
    if choice == 'espresso':
        check_resource_levels(choice)
    elif choice == 'latte':
        check_resource_levels(choice)
    elif choice == 'cappuccino':
        check_resource_levels(choice)
    elif choice == 'report':
        # TODO: 3a. When the user enters 'report', a report should be generated that shows the current resource values.
        get_report()
        print(f"Money: {sales_profit}")
    else:
        print("Please enter a valid choice.")

    # TODO: 5. Process coins.
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels:? "))
    pennies = int(input("how many pennies:? "))

    # TODO: 5b. Calculate value of coins inserted.
    total_value = float((quarters * .25) + (dimes * .10) + (nickels * 0.05) + (pennies * .01))
    change = 0.0
    # TODO: 6. Check the total value of inserted coins to ensure they are >= to the drink cost.
    if total_value == MENU[choice]["cost"]:
        # TODO: 6b. If total coins value is enough, the value of the drink gets added to the machine's total profit.
        sales_profit += total_value
        print(f"Here is ${change} in change. ")
        # TODO: 7d. Print "Here is your {drink}"
        print(f"Here is your {choice}. Enjoy!")
    elif total_value > MENU[choice]["cost"]:
        # TODO: 6c. If the user inserted too much money, the machine should give them change.
        sales_profit += MENU[choice]["cost"]
        difference = total_value - MENU[choice]["cost"]
        change += difference
        print(f"Here is ${change} in change. ")
        # TODO: 7d. Print "Here is your {drink}"
        print(f"Here is your {choice}. Enjoy!")
    else:
        # TODO: 6a. If total coins value is less than drink cost, print "Sorry, that is not enough money. Money refunded."
        print("Sorry, that's not enough money. Money refunded.")

# TODO: 7. Make the coffee.
# TODO: 7b. If the money transaction was successful and there are enough resources for the selected drink, the
#           resources should be deducted from the resource totals.
# TODO: 7c. Updated resource totals.
