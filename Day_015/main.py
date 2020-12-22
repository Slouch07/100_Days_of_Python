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

# TODO: 1. Ask user what they would like? (espresso/latte/cappuccino/off/report).
powered_on = True
# TODO: 1b. The prompt should show every time an action has been completed. eg) Once the drink has dispensed.
while powered_on:
    choice = input("What would you like? (espresso: $1.50/latte: $2.50/cappuccino $3.00: ").lower()
# TODO: 1a. Check the user's input to decide what to do next.
    # TODO: 2. Turn the coffee machine off by entering 'off' in the prompt.
    if choice == 'off':
        powered_on = False
    elif choice == 'espresso':
        #do something
    elif choice == 'latte':
        #do something
    elif choice == 'cappuccino':
        #do something
    elif choice == 'report':
        # TODO: 3a. When the user enters 'report', a report should be generated that shows the current resource values.
        #do something


# TODO: 4. Check if the resources are sufficient for user's order.
# TODO: 4b. If any resources are insufficient for that particular drink, print "Sorry there is not enough {resource}.
# TODO: 5. Process coins.
# TODO: 5a. If there are sufficient resources to make the selected drink, prompt the user to insert coins.
# TODO: 5b. Calculate value of coins inserted.
# TODO: 6. Check the total value of inserted coins to ensure they are >= to the drink cost.
# TODO: 6a. If total coins value is less than drink cost, print "Sorry, that is not enough money. Money refunded."
# TODO: 6b. If total coins value is enough, the value of the drink gets added to the machine's total profit.
# TODO: 6c. If the user inserted too much money, the machine should give them change.
# TODO: 7. Make the coffee.
# TODO: 7b. If the money transaction was successful and there are enough resources for the selected drink, the
#           resources should be deducted from the resource totals.
# TODO: 7c. Updated resource totals.
# TODO: 7d. Print "Here is your {drink}"