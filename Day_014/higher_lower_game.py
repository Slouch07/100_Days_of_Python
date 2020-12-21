# Import modules
import art, game_data, random, replit

def select_entity(list):
  entity = random.choice(list)
  return entity

def get_entity_info(entity_info):
  name = entity_info["name"]
  description = entity_info["description"]
  country = entity_info["country"]
  return(f"{name}, a {description}, from {country}.")


# Create a list for the selected entities.
random_entities = []
score = 0

entity_a = select_entity(game_data.data)
random_entities.append(entity_a)

# If the two random entries are the same entry choose again.
entity_b = select_entity(game_data.data)

game_over = False
while not game_over:
  # Print logo art
  print(art.logo)

  while entity_a == entity_b:
    entity_b = select_entity(game_data.data)
  random_entities.append(entity_b)
  
  # Print 'compare A' dictionary contents.
  print(f"Compare A: {get_entity_info(random_entities[0])}")

  # Print 'vs' logo art
  print(art.vs)

  # Print 'agaist B' dictionary contents.
  print(f"Against B: {get_entity_info(random_entities[1])}")

  # Ask use to guess who has more followers. A or B
  player_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  # Compare follower_counts in each case.
  # Store follower count for each entity
  follower_count_a = random_entities[0]["follower_count"]
  follower_count_b = random_entities[1]["follower_count"]

  # If right - print 'you're right!' and score total.
  # Swap contents of 'B' to postion 'A'and repeat steps above.
  if player_guess == 'a' and follower_count_a > follower_count_b:
    score += 1
    random_entities.pop(1)
    entity_b = select_entity(game_data.data)
    random_entities.append(entity_b)
    replit.clear()
    print(f"You're right! Score: {score}.")
  elif player_guess == 'b' and follower_count_b > follower_count_a:
    score += 1
    random_entities.pop(0)
    entity_b = select_entity(game_data.data)
    random_entities.append(entity_b)
    replit.clear()
    print(f"You're right! Score: {score}.")
  else:
    # If wrong - clear game contents and print 'Sorry, that's wrong. Final {score}.
    # End the game.
    game_over = True
    replit.clear()
    print(f"Sorry, that's wrong. Final score: {score}.")

  
