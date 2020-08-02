from unittest import TestCase
from unittest.mock import patch
from GameCards_OriHasin.DeckOfCards import DeckOfCards
from GameCards_OriHasin.Player import Player

class TestPlayer(TestCase):
    def setUp(self):
        self.Player1=Player('Ori',1600)
    def test_set_hand(self):
        with patch('GameCards_OriHasin.DeckOfCards.DeckOfCards.dealOne') as dealOne_mocked:
            self.Deck1=DeckOfCards()
            self.Player1.setHand(self.Deck1)
            dealOne_mocked.assert_called_with()

    def test_get_card(self):
        pass

    def test_add_card(self):
        pass

    def test_reduce_amount(self):
        pass

    def test_add_amount(self):
        pass
