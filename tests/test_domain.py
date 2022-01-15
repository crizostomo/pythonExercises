from unittest import TestCase
from Alura_Exercises.auction_test.domain import User, Bid, Auction
from Alura_Exercises.auction_test.exceptions import InvalidBid


class TestAssessor(TestCase):
    def setUp(self):
        self.diogo = User("Dg", 500)
        self.yuri = User("Yr", 500)
        self.yuri_bid = Bid(self.yuri, 100)
        self.diogo_bid = Bid(self.diogo, 150)
        self.auction = Auction("Cellphone")

    def test_should_not_allow_to_input_a_bid_in_decreasing_order(self):

        with self.assertRaises(InvalidBid):
            self.auction.input(self.diogo_bid)
            self.auction.input(self.yuri_bid)

    def test_return_the_highest_and_lowest_value_in_a_bid_in_increasing_order(self):
        self.auction.input(self.yuri_bid)
        self.auction.input(self.diogo_bid)

        lowest_value_expected = 100
        highest_value_expected = 150

        self.assertEqual(lowest_value_expected, self.auction.lowest_bid)
        self.assertEqual(highest_value_expected, self.auction.highest_bid)

    def test_return_the_same_value_when_the_bid_has_one_bid(self):
        self.auction.input(self.diogo_bid)

        self.assertEqual(150, self.auction.lowest_bid)
        self.assertEqual(150, self.auction.highest_bid)

    def test_return_the_highest_and_lowest_value_in_a_bid_that_has_three_bids(self):
        peter = User("Pt", 500)

        peter_bid = Bid(peter, 250)

#        auction = Auction("Cellphone")

        self.auction.input(self.yuri_bid)
        self.auction.input(self.diogo_bid)
        self.auction.input(peter_bid)

        lowest_value_expected = 100
        highest_value_expected = 250

        self.assertEqual(lowest_value_expected, self.auction.lowest_bid)
        self.assertEqual(highest_value_expected, self.auction.highest_bid)

    def test_allow_to_bid_if_there_is_no_bid(self):
        self.auction.input(self.yuri_bid)

        quantity_of_bids = len(self.auction.bids)
        self.assertEqual(1, quantity_of_bids)

    def test_allow_to_bid_if_the_last_user_different(self):
        yuri = User("Yuri", 500)
        yuri_bid = Bid(yuri, 200)

        self.auction.input(self.yuri_bid)
        self.auction.input(yuri_bid)

        quantity_of_bids = len(self.auction.bids)

        self.assertEqual(2, quantity_of_bids)

    def test_not_allow_if_user_the_same(self):
        diogo_bid = Bid(self.diogo, 200)

        with self.assertRaises(InvalidBid):
            self.auction.input(self.diogo_bid)



