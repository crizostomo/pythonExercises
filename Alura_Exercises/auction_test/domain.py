from Alura_Exercises.auction_test.exceptions import InvalidBid


class User:

    def __init__(self, name, wallet):
        self.__name = name
        self.__wallet = wallet

    def input_bid(self, auction, value):
        if not self._value_is_valid(value):
            raise InvalidBid("It cannot to input bid")

        value = Bid(self, value)
        auction.input(Bid)

        self.__wallet -= value

    @property
    def name(self):
        return self.__name

    @property
    def wallet (self):
        return self.__wallet

    def _value_is_valid(self, value):
        return value <= self.__wallet


class Bid:

    def __init__(self, user, value):
        self.user = user
        self.value = value

class Auction:

    def __init__(self, description):
        self.description = description
        self.__bids = []
        self.highest_bid = 0
        self.lowest_bid = 0

    def input(self, bid: Bid):
        if self._bid_is_valid(bid):
            if not self._has_bids():
                self.lowest_bid = bid.value

            self.highest_bid = bid.value

            self.__bids.append(bid)


    @property
    def bids(self):
        return self.__bids[:]

    def _has_bids(self):
        return self.__bids

    def _different_users(self, bid):
        if self.__bids[-1].user != bid.user:
            return True
        raise InvalidBid("The same user cannot input two followed bids")

    def _value_higher_than_previous(self, bid):
        if bid.value > self.__bids[-1].value:
            return True
        raise InvalidBid("The value must be higher than the previous one")

    def _bid_is_valid(self, bid):
        return not self.__bids or (self._different_users(bid) and
                                   self._value_higher_than_previous(bid))



