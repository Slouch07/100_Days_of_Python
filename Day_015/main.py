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


def check_resource_levels(user_input):
    """Check if the resources are sufficient for user's order."""
    if user_input == "espresso":
        if MENU["espresso"]["ingredients"]["water"] > resources["water"]:
            low_item = "water"
            print(f"Sorry, there is not enough {low_item}.")
            return False
        elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
            low_item = "coffee"
            print(f"Sorry, there is not enough {low_item}.")
            return False
        else:
            return True
    elif MENU[user_input]["ingredients"]["water"] > resources["water"]:
        low_item = "water"
        print(f"Sorry, there is not enough {low_item}.")
        return False
    elif MENU[user_input]["ingredients"]["milk"] > resources["milk"]:
        low_item = "milk"
        print(f"Sorry, there is not enough {low_item}.")
        return False
    elif MENU[user_input]["ingredients"]["coffee"] > resources["coffee"]:
        low_item = "coffee"
        print(f"Sorry, there is not enough {low_item}.")
        return False
    else:
        print(f"Please insert coins")
        return True


def deduct_resources(selected_drink):
    """Deducts resouces after a coffee has been selected."""
    if selected_drink == "espresso":
        resources["water"] -= MENU[selected_drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[selected_drink]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[selected_drink]["ingredients"]["water"]
        resources["milk"] -= MENU[selected_drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[selected_drink]["ingredients"]["coffee"]


# Variable to keep track of the profit generated.
sales_profit = 0

powered_on = True
while powered_on:
    sufficient_resources = False
    # Loop to check user's choice and levels of required resources.
    while not sufficient_resources:
        choice = input(
            " What would you like? (espresso: $1.50/latte: $2.50/cappuccino $3.00): ").lower()
        if choice == 'off':
            # Breaks out of inner loop if user selects "off"
            break
        if choice == 'espresso':
            sufficient_resources = check_resource_levels(choice)
        elif choice == 'latte':
            sufficient_resources = check_resource_levels(choice)
        elif choice == 'cappuccino':
            sufficient_resources = check_resource_levels(choice)
        elif choice == 'report':
            get_report()
            print(f"Money: ${sales_profit}")
        else:
            print("Please enter a valid choice.")

    # Breaks out of outer loop if user selects "off"
    if choice == 'off':
        break
    else:
        # If user selects a drink and resources are available this logic will ask for money.
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickels = int(input("how many nickels:? "))
        pennies = int(input("how many pennies:? "))

        # Calculate the value of the inserted coins.
        total_value = float((quarters * .25) + (dimes * .10) +
                            (nickels * 0.05) + (pennies * .01))

        # Variable to store any over payment.
        change = 0.0

        # Determines if the value is equal, too much or too little.
        if total_value == MENU[choice]["cost"]:
            sales_profit += total_value
            print(f"Here is ${change} in change. ")
            print(f"Here is your {choice}. Enjoy!")
        elif total_value > MENU[choice]["cost"]:
            # If the user inserted too much money, the machine should give them change.
            sales_profit += MENU[choice]["cost"]
            difference = total_value - MENU[choice]["cost"]
            change += difference
            print(f"Here is ${round(change,1)} in change. ")
            print(f"Here is your {choice}. Enjoy!")
        else:
            print("Sorry, that's not enough money. Money refunded.")

        # Updated resource totals.
        deduct_resources(choice)
