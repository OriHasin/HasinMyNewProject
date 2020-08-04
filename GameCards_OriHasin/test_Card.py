from unittest import TestCase
from GameCards_OriHasin.Card import Card
class TestCard(TestCase):

    def test_repr_(self):#בדיקה לפונקציית הדפסת אובייקט
        self.card1=Card('♣','Ace')
        self.assertIn('Ace',self.card1.__repr__())

    def test_gt1(self):#בדיקה שהפונקציה מחזירה True של קלף גדול על סמך ערך
        self.card1 = Card('♣', 'Ace')
        self.card2 = Card('♣', '2')
        self.assertTrue(self.card1>self.card2)

    def test_gt2(self):#בדיקה שהפונקציה מחזירה True של קלף גדול על סמך סמל
        self.card1 = Card('♣', '2')
        self.card2 = Card('♦', '2')
        self.assertTrue(self.card1>self.card2)

    def test_gt3(self):#דגש בדיקה שהפונקציה מחזירה False של קלף קטן על סמך ערך
        self.card1 = Card('♣', '2')
        self.card2 = Card('♦', '4')
        self.assertFalse(self.card1>self.card2)

    def test_gt4(self):#בדיקה שהפונקציה מחזירה False של קלף קטן על סמך סמל
        self.card1 = Card('♦','2')
        self.card2 = Card('♣','2')
        self.assertFalse(self.card1>self.card2)



