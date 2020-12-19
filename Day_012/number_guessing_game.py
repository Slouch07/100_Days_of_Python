import art, random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def generate_number():
  """Selects a random number between 1 and 100"""
  number = random.randint(1, 100)
  return number

easy_guesses = 10
hard_guesses = 5
game_number = generate_number()

# Game logic
game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if game_mode == 'easy':
  print(f"You have {guesses} attempts remaining to guess the number.")
  # easy_game()...will play with 10 guesses max.
  
else:
  print(f"You have {guesses} attempts remaining to guess the number.")
  # hard_game()...will play with 5 guesses max.

player_guess = input("Please guess a number: ")
if guesses == 0:
  print("You've run out of guesses, you lose.")
elif player_guess > game_number:
  guesses -= 1
  print("Too high.")
  print("Guess again.")
  print(f"You have {guesses} attempts remaining to guess the number.")
elif player_guess < game_number:
  guesses -= 1
  print("Too low.")
  print("Guess again.")
  print(f"You have {guesses} attempts remaining to guess the number.")
else:
  print(f"You got it! The number was {game_number}")



