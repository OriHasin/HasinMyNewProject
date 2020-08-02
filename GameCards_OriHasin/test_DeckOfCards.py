from unittest import TestCase
from GameCards_OriHasin.Card import Card
from GameCards_OriHasin.DeckOfCards import DeckOfCards
class TestDeckOfCards(TestCase):
    def setUp(self):
        self.Deck1=DeckOfCards()
    def test_shuflle1(self):#בדיקה שהפונקציה מבצעת ערבוב
        self.First = self.Deck1.list3[0]
        self.Deck1.Shuflle()
        self.assertNotEqual(self.Deck1.list3[0],self.First)
    def test_shuffle2(self):#בדיקה שהפונקציה לא מבצעת ערבוב במהלך משחק
        self.First = self.Deck1.list3[0]
        self.Deck1.list3.remove(self.Deck1.list3[-1])
        self.Deck1.Shuflle()
        self.assertEqual(self.Deck1.list3[0],self.First)
    def test_deal_one1(self):#בדיקה שהפונקציה מחזירה את הקלף האחרון בחפיסה
        self.Last=self.Deck1.list3[-1]
        self.assertEqual(self.Deck1.list3.pop(),self.Last)
    def test_deal_one2(self):#בדיקה שהפונקציה עדכנה את החפיסה ל-51
        self.Deck1.list3.pop()
        self.assertEqual(len(self.Deck1.list3),51)
    def test_new_game1(self):#בדיקה שהפונקציה יוצרת חפיסה חדשה
        self.Deck1.list3=self.Deck1.list3[:16]
        self.Deck1.newGame()
        self.assertEqual(len(self.Deck1.list3),52)
    def test_new_game2(self):#בדיקה שהפונקציה מבצעת ערבוב לחפיסה
        self.First=self.Deck1.list3[0]
        self.Deck1.newGame()
        self.assertNotEqual(self.Deck1.list3[0],self.First)



