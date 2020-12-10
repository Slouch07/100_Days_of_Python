# A Rock, Paper, Scissor game in Python.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Ask player to choose a move.
players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if players_choice < 0 or players_choice > 2: 
  print("Invalid choice, you lose. Please select 0, 1, or 2.")
else:  
  if players_choice == 0:
    players_choice = rock
    print(rock)
  elif players_choice == 1:
    players_choice = paper
    print(paper)
  elif players_choice == 2:
    players_choice = scissors
    print(scissors)
    
  # Have the computer choose a move.
  print("Computer Chose:")
  moves = [rock, paper, scissors]
  computers_choice = random.choice(moves)
  print(computers_choice)

  # Logic to decide who wins.
  if (players_choice == rock) and (computers_choice == paper):
    print("You lose")
  elif (players_choice == paper) and (computers_choice == scissors):
    print("You Lose")
  elif (players_choice == scissors) and (computers_choice == rock):
    print("You Lose")
  elif players_choice == computers_choice:
    print("You Tie")
  else:
    print("You Win!")