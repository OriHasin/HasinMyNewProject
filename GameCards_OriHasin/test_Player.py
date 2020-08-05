from unittest import TestCase
from unittest.mock import patch
from GameCards_OriHasin.DeckOfCards import DeckOfCards
from GameCards_OriHasin.Card import Card
from GameCards_OriHasin.Player import Player

class TestPlayer(TestCase):
    def setUp(self):
        self.Player1=Player('Ori',1600)

    def test_init1(self):#בדיקת התנאי , לא נכנס לי שם ריק
        try:
            self.Player2=Player('',1600)
        except:
            pass
        else:
            self.fail()

    def test_init2(self):#בדיקה שלא מתקבל מס קלפים שלילי
        try:
            self.Player2=Player('Ori',1600,-1)
        except:
            pass
        else:
            self.fail()

    def test_init3(self):#בדיקה שלא מתקבל מס קלפים '0'
        try:
            self.Player2=Player('Ori',1600,0)
        except:
            pass
        else:
            self.fail()

    def test_repr_(self):#בדיקה לפונקציית הדפסת אובייקט
        self.assertIn('Ori',self.Player1.__repr__())

    def test_set_hand1(self):#בדיקה שהפונקציה מכניסה קלף לחבילה האישית של המשתמש
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

    def test_set_hand3(self):#בדיקה שהפונקציה מכניסה NumOfCards קלפים לחבילת השחקן
        self.Deck1=DeckOfCards()
        self.Player1.setHand(self.Deck1)
        self.assertEqual(len(self.Player1.list1),self.Player1.NumOfCards)

    def test_get_card1(self):#בדיקה שהקלף האחרון מחבילת המשתמש אכן נשלף ואורך הרשימה התעדכן
        self.Deck1=DeckOfCards()
        self.Player1.setHand(self.Deck1)
        self.last=self.Player1.list1[-1]
        self.assertEqual(self.last,self.Player1.getCard())
        self.assertEqual((len(self.Player1.list1)),4)

    def test_get_card2(self):#בדיקה שלא נשלף קלף אם החבילה האישית של השחקן ריקה
        try:
            self.Player1.getCard()
        except:
            pass
        else:
            self.fail()

    def test_add_card1(self):#בדיקה שהקלף מתווסף לחבילת הקלפים של השחקן
        self.card1=Card("♣","Ace")
        self.Deck1=DeckOfCards()
        self.Player1.setHand(self.Deck1)
        self.Player1.addCard(self.card1)
        self.assertEqual(self.Player1.list1[-1],self.card1)

    def test_add_card2(self):#בדיקה שהאובייקט המתקבל הוא מסוג קלף
        try:
            self.Player1.addCard(2)
        except:
            pass
        else:
            self.fail()

    def test_reduce_amount1(self):#בדיקה שסכום השחקן מתעדכן לאחר חיסור הסכום המתקבל
        self.Player1.Amount=8000
        self.Player1.reduceAmount(800)
        self.assertEqual(self.Player1.Amount,7200)

    def test_reduce_amount2(self):#בדיקה שלא מתקבל בפונקציה סכום שלילי
        try:
            self.Player1.reduceAmount(-800)
        except:
            pass
        else:
            self.fail()

    def test_reduce_amount3(self):#בדיקה שלא מתקבל בפונקציה סכום '0'
        try:
            self.Player1.reduceAmount(0)
        except:
            pass
        else:
            self.fail()

    def test_reduce_amount4(self):#בדיקה שהפונקציה מקבלת אך ורק מספר שלם
        try:
            self.Player1.reduceAmount(80.20)
        except:
            pass
        else:
            self.fail()

    def test_reduce_amount5(self):#בדיקה שסכום השחקן לא נהיה שלילי
        self.Player1.Amount=8000
        self.Player1.reduceAmount(16000)
        self.assertEqual(self.Player1.Amount,0)

    def test_add_amount1(self):#בדיקה שהפונקציה מוסיפה את הסכום המתקבל לסכום השחקן
        self.Player1.Amount=8000
        self.Player1.addAmount(8000)
        self.assertEqual(self.Player1.Amount,16000)

    def test_add_amount2(self):#בדיקה שהערך המתקבל מסוג מספר שלם בלבד
        try:
            self.Player1.addAmount(8000.8)
        except:
            pass
        else:
            self.fail()

    def test_add_amount3(self):#בדיקה שלא מתקבל פרמטר שלילי
        try:
            self.Player1.addAmount(-8000)
        except:
            pass
        else:
            self.fail()

    def test_add_amount4(self):#בדיקה שלא מתקבל פרמטר '0'
        try:
            self.Player1.addAmount(0)
        except:
            pass
        else:
            self.fail()
