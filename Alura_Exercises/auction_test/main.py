from domain import User, Bid, Auction, Assessor

diogo = User("Dg")
yuri = User("Yr")

yuri_bid = Bid(yuri, 100)
diogo_bid = Bid(diogo, 150)

auction = Auction("Cellphone")

auction.bids.append(diogo_bid)
auction.bids.append(yuri_bid)

for bid in auction.bids:
    print(f'The user {bid.user.name} gave a bid of {bid.value}')

assessor = Assessor()
assessor.assess(auction)

print(f'the lowest bid was {assessor.lowest_bid} and the highest bid was {assessor.highest_bid} ')