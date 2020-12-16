# https://repl.it/@Slouch07/blind-auction-start-Silent-Auction-Project#main.py
from replit import clear
import art
# Create an empty dictionary
bid_entries = {}
# Import and print the logo from art.py module
print(art.logo)
# Set a variable to true to allow are loop to continue if it's true.
bidding = True
while bidding:
    # Ask the user for their name and store it in a variable.
    name_of_bidder = input("What is your name?: ")
    # Ask the user for their bid amount and store it in a variable.
    amount_of_bid = int(input("What is your bid amount?: $"))
    # Add the users inputs to the dictionary. Their name as the key and their bid as the value.
    bid_entries[name_of_bidder] = amount_of_bid
    # Ask the user if there are other bidders and if there is repeat the steps above. If there are not then the loop is broken.
    another_bid = input("Would someone else like to bid? 'yes' or 'no': ").lower()
    if another_bid == 'yes':
        clear()
    elif another_bid == 'no':
        bidding = False
        clear()
# Place bid values from dictionary into a list.
bids = list(bid_entries.values())
# Place bidder names in a list.
names = list(bid_entries.keys())
# Determine the largest bid amount.
highest_bid = max(bids)
# Determine the name of the user with the largest bid.
bid_winner = names[bids.index(highest_bid)]
# Output the winner and their bid to the console.
print(f"The winner is {bid_winner} with a bid of ${highest_bid}.")

# Angela's more condensed code for determining winning bid and winner's name.
# def get_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#         print(f"The winner is {bid_winner} with a bid of ${highest_bid}.")