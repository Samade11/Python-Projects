from Auction_Art import logo
print(logo)
import os

bids = {}
biding_finished = False

def find_highestest_bider(bidding_record):
    highest_bid = 0
    winner = ""
    {"Sam": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with the bid of £{highest_bid}")
while not biding_finished:
    name = input("What is your name?\n")
    price = int(input("What price would you like to bid?\n£"))
    bids [name] = price
    should_continue = input("Is there anyone else that would like to bid type 'YES' or 'No'").lower()
    if should_continue == "no":
        biding_finished = True
        find_highestest_bider(bids)
    elif should_continue == "yes":
        os.system('cls')