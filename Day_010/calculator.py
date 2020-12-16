import art

# Addition
def get_sum(a, b):
  """Take two numbers as inputs and finds the sum."""
  return a + b

# Subtraction
def get_difference(a, b):
  """Takes two numbers as inputs and finds the difference."""
  return a - b

# Multiplication
def get_product(a, b):
  """Takes two numbers as inputs and finds the product."""
  return a * b

# Division
def get_quotient(a, b):
  """Takes two numbers as inputs and finds the quotient."""
  return a / b

# Dictionary to hold operation symbols and their function.
operations = {
  "+": get_sum,
  "-": get_difference,
  "*": get_product,
  "/": get_quotient,
}

# An example of recursion where the entire program is put in a function and then can call itself.
def calculating():
  # Import the ASCII art from the art.py file.
  print(art.logo)
  # Ask the user for a number and store it.
  num1 = float(input("What's the first number?: "))
  # Iterate over the 'keys' and print them to console.
  for operation in operations:
    print(operation)
  # Loop which continues if a user wants to do another calculation using the last answer.
  continue_calculating = True
  while continue_calculating:
    # Ask the user for the operation to perform and the next number.
    operation_symbol = input("Which operation would like to perform?: ")
    num2 = float(input("What's the next number?: "))
    # Grabs the operation function (value) from the dictionary and stores it in a variable.
    calculation = operations[operation_symbol]
    # Uses the stored function from prior step to calculate result, stores it in a variable.
    answer = calculation(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    # Asks the user if they want another calculation with the previous answer or a new calculation.
    another_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
    # If 'y' the variable num1 will contain the previous answer.
    if another_calc == 'y':
      num1 = answer
    # If 'n' the loop is exited, the screen is cleared and the whole program starts over.
    else:
      continue_calculating = False
      calculating()

calculating()