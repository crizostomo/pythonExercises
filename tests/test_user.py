from Alura_Exercises.auction_test.domain import User, Auction

import pytest

from Alura_Exercises.auction_test.exceptions import InvalidBid


@pytest.fixture
def vini():
    return Auction("Cellphone")


@pytest.fixture
def auction():
    return User("Vini", 100)


def test_withdraw_value_from_user_when_input_bid(vini, auction):
    vini.input_bid(auction, 50)

    assert vini.wallet == 50

def test_allow_to_input_bid_when_value_less_than_wallet(vini, auction):
    vini.input_bid(auction, 1)

    assert vini.wallet == 99

def test_allow_to_input_bid_when_value_equals_to_value_in_wallet(vini, auction):
    vini.input_bid(auction, 100)

    assert vini.wallet == 0

def test_not_allow_to_input_bid_when_value_higher_than_value_in_wallet(vini, auction):
    with pytest.raises(InvalidBid):

        vini.input_bid(auction, 200)
