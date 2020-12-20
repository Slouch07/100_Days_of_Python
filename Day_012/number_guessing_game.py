import art, random, replit
def guess_number():
  def generate_number():
    """Selects a random number between 1 and 100"""
    number = random.randint(1, 101)
    return number
  # Prints ASCII art to consol
  print(art.logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  # Initialize variables used in main game logic.
  guesses_remaining = 0
  game_number = generate_number()

  # Game logic
  game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if game_mode == 'easy':
    guesses_remaining = 10  
  else:
    guesses_remaining = 5
  # Until the user wins or runs out of guesses they will be asked to guess a number.
  game_over = False
  while not game_over:
      print(f"You have {guesses_remaining} attempts remaining to guess the number.")
      player_guess = int(input("Please guess a number: "))
      guesses_remaining -= 1
      if guesses_remaining == 0:
        game_over = True
        print("You've run out of guesses, you lose.")
      elif player_guess > game_number:
        print("Too high.")
        print("Guess again.")
      elif player_guess < game_number:
        print("Too low.")
        print("Guess again.")
      else:
        game_over = True
        print(f"You got it! The number was {game_number}.")
  # Code to play another game.
  restart = input("Would you like to play again? 'yes' or 'no': ").lower()
  if restart == 'yes':
    replit.clear()
    guess_number()
  else:
    print("Goodbye.")

guess_number()


