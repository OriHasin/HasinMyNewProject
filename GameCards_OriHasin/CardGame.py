from GameCards_OriHasin.Card import Card
from GameCards_OriHasin.DeckOfCards import DeckOfCards
from GameCards_OriHasin.Player import Player
from random import *
class CardGame:

    #מחלקה היוצרת משחק קלפים , מגדירה 4 שחקנים וחפיסת קלפים אחת
    #NumOfCards,Amount, ListPlayers = רשימה של השחקנים המשתתפים

    def __init__(self,NumOfCards=5): #מתודת קונסטרקטור
        Amount=randint(5000,10000)
        self.Deck=DeckOfCards()
        self.NumOfCards=NumOfCards
        self.Player1=Player('Ori',Amount)
        self.Player2=Player('Ziv',Amount)
        self.Player3=Player('Roy',Amount)
        self.Player4=Player('Orly',Amount)
        self.listPlayers=[self.Player1,self.Player2,self.Player3,self.Player4]
        self.newGame()
        for i in self.listPlayers:
            i.Print()

    def newGame(self): #מתודה המערבבת חפיסת קלפים ומחלקת קלפים ל-4 שחקנים
        self.Deck.Shuflle()
        for i in self.listPlayers:
            i.NumOfCards=self.NumOfCards #מספר קלפים עדכני שיחולק לכל שחקן
            i.setHand(self.Deck.list3)
a=CardGame()








