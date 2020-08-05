from GameCards_OriHasin.DeckOfCards import DeckOfCards
from GameCards_OriHasin.Player import Player
from random import *
class CardGame:

    #מחלקה היוצרת משחק קלפים , מגדירה 4 שחקנים וחפיסת קלפים אחת
    #NumOfCards,Amount, ListPlayers = רשימה של השחקנים המשתתפים

    def __init__(self,NumOfCards=5): #מתודת קונסטרקטור
        self.Amount=randint(5000,10000)
        self.Deck=DeckOfCards()
        self.NumOfCards=NumOfCards
        if self.NumOfCards<=0:#בדיקה שלא מתקבל מס' קלפים '0' או שלילי
            raise ValueError("Enter a positive number of cards")
        self.Player1=Player(input("Enter name of player: "),self.Amount)
        self.Player2=Player(input("Enter name of player: "),self.Amount)
        self.Player3=Player(input("Enter name of player: "),self.Amount)
        self.Player4=Player(input("Enter name of player: "),self.Amount)
        self.listPlayers=[self.Player1,self.Player2,self.Player3,self.Player4]
        self.newGame()
        for i in self.listPlayers:#הדפסת פרטים של שחקן
            print(i.__repr__())

    def newGame(self): #מתודה המערבבת חפיסת קלפים ומחלקת קלפים ל-4 שחקנים
        if len(self.Deck.list3)<52:
            raise ValueError("You are in a middle of a game")
        self.Deck.Shuflle()
        for i in self.listPlayers:
            i.NumOfCards=self.NumOfCards #מספר קלפים עדכני שיחולק לכל שחקן,יתעדכן במצב של שונה מ-5
            i.setHand(self.Deck)










