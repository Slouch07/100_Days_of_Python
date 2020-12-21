# Import modules
import art, game_data, random, replit

def select_entity(list):
  """Selects a random entry from the data list."""
  entity = random.choice(list)
  return entity

def get_entity_info(entity_info):
  """Selects the name, description, and country from the entry."""
  name = entity_info["name"]
  description = entity_info["description"]
  country = entity_info["country"]
  return(f"{name}, a {description}, from {country}.")

# Create a list for the selected entities.
random_entities = []

# Variable to contain players score.
score = 0

# Select entry for entity A and append to random_entities list.
entity_a = select_entity(game_data.data)
random_entities.append(entity_a)

# Select entry for entity B random_entities list.
entity_b = select_entity(game_data.data)
random_entities.append(entity_b)

game_over = False
while not game_over:
  
  # Print logo art
  print(art.logo)

  # If right - print 'you're right!' and score total.
  if score > 0:
    print(f"You're right! Score: {score}.")

  # If entry A and entry B are the same, re-select entry B.
  if random_entities[0] == random_entities[1]:
    random_entities.remove(entity_b)
    entity_b = select_entity(game_data.data)
    random_entities.append(entity_b)
  
  # Print 'compare A' dictionary contents.
  print(f"Compare A: {get_entity_info(random_entities[0])}")

  # Print 'vs' art
  print(art.vs)

  # Print 'agaist B' dictionary contents.
  print(f"Against B: {get_entity_info(random_entities[1])}")

  # Ask use to guess who has more followers. A or B
  player_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  # Compare follower_counts in each case.
  # Store follower count for each entity
  follower_count_a = random_entities[0]["follower_count"]
  follower_count_b = random_entities[1]["follower_count"]

  # Swap contents of 'B' to postion 'A'and repeat steps above.
  if player_guess == 'a' and follower_count_a > follower_count_b:
    score += 1
    random_entities.pop(1)
    entity_b = select_entity(game_data.data)
    random_entities.append(entity_b)
    replit.clear()
  elif player_guess == 'b' and follower_count_b > follower_count_a:
    score += 1
    random_entities.pop(0)
    entity_b = select_entity(game_data.data)
    random_entities.append(entity_b)
    replit.clear()
  else:
    # If wrong - clear game contents and print 'Sorry, that's wrong. Final {score}.
    # End the game.
    game_over = True
    replit.clear()
    print(f"Sorry, that's wrong. Final score: {score}.")

  
