# A program that outputs a band name after the user provides the city they grew up in
# and the name of a pet.

# Greets the user to the program.
print("Welcome to the Band Name Generator!!")

# Asks the user for the city that they grew up in.
city = input("What city did you grow up in?\n")

# Asks the user for the name of a pet.
pet = input("What is the name of a pet?\n")

# Combines their input and prints their band name.
band_name = city + " " + pet
print("Your new band name could be: " + band_name)