from unittest import TestCase
from GameCards_OriHasin.CardGame import CardGame
from GameCards_OriHasin.DeckOfCards import DeckOfCards
from unittest.mock import patch

class TestCardGame(TestCase):
    def setUp(self):
        self.CardGame1=CardGame()

    def test_init1_(self):#בדיקה שלא מקבלת מס' קלפים שלילי
        try:
            self.CardGame2=CardGame(-2)
        except:
            pass
        else:
            self.fail()

    def test_init2_(self):#בדיקה שלא מקבלת מס' קלפים '0'
        try:
            self.CardGame2 = CardGame(0)
        except:
            pass
        else:
            self.fail()

    def test_init3_(self):#בדיקה שהקונסטרקטור הגדיר 4 שחקנים
        self.assertEqual(len(self.CardGame1.listPlayers),4)

    def test_init4_(self):#בדיקה שהקונסטרקטור הגדיר חפיסת קלפים
        if type(self.CardGame1.Deck)==DeckOfCards:
            pass
        else:
            self.fail()

    def test_init5_(self):#בדיקה שסכום הכסף שווה בין כל השחקנים
        for i in range (len(self.CardGame1.listPlayers)):
            self.assertEqual(self.CardGame1.listPlayers[i].Amount,self.CardGame1.Amount)

    def test_init6(self):#בדיקה שהקונסטרקטור מדפיס פרטי שחקן
        for i in range(4):
            self.assertIn(self.CardGame1.listPlayers[i].Name,self.CardGame1.listPlayers[i].__repr__())

    def test_init7_(self):#בדיקה שהפונקציה newGame נקראת בקונסטרקטור
        with patch('GameCards_OriHasin.CardGame.CardGame.newGame') as new_game_mocked:
            self.CardGame2=CardGame()
            new_game_mocked.assert_called_with()

    def test_newGame1(self):#בדיקה שהפונקציה Shuffle נקראת דרך ה-newGame
        with patch('GameCards_OriHasin.DeckOfCards.DeckOfCards.Shuflle') as mocked_Shuffle:
            self.CardGame2=CardGame()
            mocked_Shuffle.assert_called_with()

    def test_newGame2(self):#בדיקה שהפונקציה קוראת ל-setHand בכדי לחלק קלפים לשחקנים
        with patch('GameCards_OriHasin.Player.Player.setHand') as mocked_setHand:
            self.CardGame2=CardGame()
            mocked_setHand.assert_called_with(self.CardGame2.Deck)

    def test_newGame3(self):#בדיקה שהפונקציה מתבצעת אך ורק על חפיסה מלאה
        self.CardGame1.Deck.list3=self.CardGame1.Deck.list3[:16]
        try:
            self.CardGame1.newGame()
        except:
            pass
        else:
            self.fail()
