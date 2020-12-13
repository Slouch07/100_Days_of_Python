import random, hangman_art, hangman_words

# A random word is selected from our list of words.
chosen_word = random.choice(hangman_words.word_list)

#Initialize variables.
lives = 6
display = []
guessed_letters = []
str = ''

#Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

# Places an underscore for each element in the word and stores it in a variable.
for letter in chosen_word:
    display += "_"

#Main game logic.
while "_" in display:
    #Ask the user for a letter and store it in a variable.
    guess = input("Please guess a letter: ").lower()
    print(f"You guessed '{guess}'.\n")
    
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"The letter '{guess}' has already been guessed.")
        continue
    
    #Iterate through the word to see if the guess matches any letters.
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    
    #If no match.
    if guess not in chosen_word:
        #If the letter is not in the word, let them know.
        print(f"Sorry, {guess} is not in the word. You lose a life")
        lives -= 1
        #Import ASCII art from hangman_art.py
        print(hangman_art.stages[lives])
    
    #Converts the display list to a string and removes the commas
    print(f"{' '.join(display)}\n")
    #When the user is out of guesses, break out of the loop.
    if lives == 0:
        break

#Logic to detemine if the user has won or lost.
if str.join(display) == chosen_word:
    print("You Win!")
else:
    print("You Lose.")
    print(f"The word was: {chosen_word}")



