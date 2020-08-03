from unittest import TestCase
from unittest.mock import patch
from GameCards_OriHasin.DeckOfCards import DeckOfCards
from GameCards_OriHasin.Card import Card
from GameCards_OriHasin.Player import Player

class TestPlayer(TestCase):
    def setUp(self):
        self.Player1=Player('Ori',1600)
    def test_set_hand1(self): #בדיקה שהפונקציה מכניסה קלף לחבילה האישית של המשתמש
        with patch('GameCards_OriHasin.DeckOfCards.DeckOfCards.dealOne') as dealOne_mocked:
            self.card1=Card("♣","Ace")
            self.Deck1 = DeckOfCards()
            dealOne_mocked.return_value = self.card1
            self.Player1.setHand(self.Deck1)
            self.assertTrue(self.Player1.list1[0]==self.card1)
            dealOne_mocked.assert_called_with()
    def test_set_hand2(self):#בדיקה שהפונקציה לא מקבלת פרמטר שלא מסוג DeckOfCards
        try:
            self.Player1.setHand(100)
        except:
            pass
        else:
            self.fail()
    def test_get_card(self):
        pass

    def test_add_card(self):
        pass

    def test_reduce_amount(self):
        pass

    def test_add_amount(self):
        pass
