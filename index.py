from replit import clear
from code import logo

print(logo)

auction_data = {}


def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with the bid amount {highest_bid}")


bidding_finished = False
while not bidding_finished:
  name = input("What is your name :\n")
  bid = int(input("What is your bid :\n"))
  auction_data[name] = bid
  bidding_process = input(
    "Are there any other bidder?Type 'yes' or  'no' :\n").lower()
  if bidding_process == "no":
    bidding_finished = True
    highest_bidder(auction_data)
  elif bidding_process == 'yes':
    clear()
