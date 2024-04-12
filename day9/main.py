from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
end_auction = False
auction_dict = {}

while not end_auction:
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  auction_dict[name] = bid
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if other_bidders == "no":
    end_auction = True
  clear()

highest_bid = 0
highest_bidder = ""
for bidder in auction_dict:
  if auction_dict[bidder] > highest_bid:
    highest_bid = auction_dict[bidder]
    highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")