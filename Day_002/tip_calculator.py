# A program that will calculate the appropriate tip amount for an individual or a group.

# Welcome the user to the calculator
print("Welcome to the tip calculator")

# Ask the user for the bill amount and store it in a variable.
bill_amount = input("What was the total bill?  $")

# Ask the user what percentage tip they would like to give.
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15?  ")

# Ask the user how many people will be splitting the bill.
customers = input("How many people to split the bill? ")

# Calculate the tip and ouput the amount for each customer.
tip_amount = (float(bill_amount) / int(customers)) * (int(tip_percent) / 100 + 1)

# Round the tip amount to two decimal points.
result = format(tip_amount, '.2f')
print(f"Each customer should pay: {result}")