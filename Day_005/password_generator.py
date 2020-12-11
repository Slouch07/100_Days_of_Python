#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level - Order of characters not random:
# Initialize an empty string variable
# password = ""
# Grab a number of random letters and add them to the password variable.
# for letter in range(0, nr_letters):
#   choice = random.choice(letters)
#   password += choice
# Grab a number of random symbols and add them to the password variable.
# for symbol in range(0, nr_symbols):
#   choice = random.choice(symbols)
#   password += choice
# Grab a number of random numbers and add them to the password variable.
# for letter in range(0, nr_numbers):
#   choice = random.choice(numbers)
#   password += choice  
# print(password)

#Hard Level - Order of characters randomised:
# Initialize an empty string variable
password = ""
# Grab a number of random letters and add them to the password variable.
for letter in range(0,nr_letters):
  password += random.choice(letters)
# Grab a number of random symbols and add them to the password variable.
for symbol in range(0,nr_symbols):
  password += random.choice(symbols)
# Grab a number of random numbers and add them to the password variable.
for letter in range(0,nr_numbers):
  password += random.choice(numbers)
# Convert string variable to a list, randomise the list and convert back
# to a string variable.
character_list = list(password)
random.shuffle(character_list) 
password = "".join(character_list)
print(f"Here is your password: {password}")