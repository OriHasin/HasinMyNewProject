from unittest import TestCase
from GameCards_OriHasin.Card import Card
class TestCard(TestCase):

    def test_gt1(self):
        self.card1 = Card('♣', 'Ace')
        self.card2 = Card('♣', '2')
        self.assertGreater(self.card1,self.card2)
    def test_gt2(self):
        self.card1 = Card('♣', '2')
        self.card2 = Card('♦', '2')
        self.assertGreater(self.card1,self.card2)
    def test_gt3(self):
        self.card1 = Card('♣', '2')
        self.card2 = Card('♦', '4')
        self.assertLess(self.card1,self.card2)



