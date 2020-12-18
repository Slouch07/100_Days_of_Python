# A Python version of Black Jack. (Dec 17/2020)
# Hopefully I will look back on this one day and think wow that's too much code and repetative but hey for a beginner
# not too shabby. :)

import art
import random
# import replit

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def black_jack():
    # Initialize empty lists and score total variables.
    player_cards = []
    computer_cards = []
    player_total = 0
    computer_total = 0

    choice = input("Would you like to play a game of Black Jack? 'y' or 'n': ").lower()

    if choice == 'y':
        # replit.clear()
        print(art.logo)
        # Randomly select two numbers from the cards list for the player.
        player_cards = random.sample(cards, 2)
        # Total up the numbers in the list.
        for card in player_cards:
            player_total += card
        # Randomly select a single number from the cards list for the computer.
        computer_cards.append(random.choice(cards))
        for card in computer_cards:
            computer_total += card
        print(f"Your cards: {player_cards} Total: {player_total}")
        print(f"Computer's first card: {computer_total}")
        # If player get 21 on first hand, deal computer hands until 17 or bust.
        if player_total == 21:
            print(f"Your final hand: {player_cards} Total: {player_total}")
            while computer_total < 17:
                computer_cards.append(random.choice(cards))
                for card in computer_cards:
                    computer_total += card
                if computer_total > 21:
                    print(
                        f"Computer's final hand: {computer_cards} Total: {computer_total}")
                    print("Computer has busted.")
                    cards[0] = 11
            if player_total == computer_total:
                print("It's a draw!")
            else:
                print("You win with a BlackJack!")
            black_jack()
        # Loop to continue asking player if they want another card if they have not busted.
        draw_again = True
        while draw_again:
            another_card = input(
                "Would you like to 'hit' or 'stay'?: ").lower()
            if another_card == "hit":
                player_cards.append(random.choice(cards))
                # Resets the player_total to zero, so that it would sum the list properly.
                if len(player_cards) > 1:
                    player_total = 0
                for card in player_cards:
                    player_total += card
                print(f"Your cards: {player_cards} Total: {player_total}")
                print(f"Computer's first card: {computer_total}")
                # If the player hits 21 or busts this code executes.
                if player_total >= 21:
                    draw_again = False
                    # Switches the number 11 to 1 in the cards list.
                    cards[0] = 1
                    print(f"Your final hand: {player_cards} Total: {player_total}")
                    while computer_total < 17:
                        computer_cards.append(random.choice(cards))
                        if len(computer_cards) > 1:
                            computer_total = 0
                        for card in computer_cards:
                            computer_total += card
                    print(f"Computer's final hand: {computer_cards} Total: {computer_total}")
                    print("You busted! You lose.")
                    black_jack()
            # If the player chooses to 'stay' this code has the computer draw until 17 or bust.
            elif another_card == "stay":
                draw_again = False
                if len(player_cards) > 1:
                    player_total = 0
                for card in player_cards:
                    player_total += card
                print(f"Your final hand: {player_cards} Total: {player_total}")
                while computer_total < 17:
                    computer_cards.append(random.choice(cards))
                    if len(computer_cards) > 1:
                        computer_total = 0
                    for card in computer_cards:
                        computer_total += card
                print(f"Computer's final hand: {computer_cards} Total: {computer_total}")
                # Code compares scores and determines the winner or if it was a draw.
                if computer_total > 21:
                    print("Computer busts. You win!")
                elif player_total > computer_total:
                    print("You win!")
                elif computer_total > player_total:
                    print("You lose!")
                else:
                    print("Draw...you live another day!")
                black_jack()
    else:
        print("Goodbye")

black_jack()
