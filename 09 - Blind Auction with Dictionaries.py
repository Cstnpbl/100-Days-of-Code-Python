loop=1
bidders = {}
while loop==1:

    name=input("What is your name?: ")
    bid=int(input("What is your bid?: $ "))

    bidders[name]=bid

    more=input("Are there any more bidders? Type 'yes' or 'no': ")
    if more.lower()=='no':
        loop=0

highest_bid=0
highest_bidder=""
for bidder in bidders:
    if bidders[bidder]>highest_bid:
        highest_bid=bidders[bidder]
        highest_bidder=bidder


print("The winner is " , highest_bidder , "with a bid of " , highest_bid)