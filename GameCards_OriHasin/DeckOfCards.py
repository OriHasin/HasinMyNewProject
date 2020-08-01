from GameCards_OriHasin.Card import Card
from random import *
class DeckOfCards:

    #מחלקה היוצרת חפיסת קלפים
    #list1 - רשימה של סוגי קלפים  list2 - רשימה של ערכי קלפים   list3 - רשימה המכילה 52 קלפים

    def __init__(self):                 #מתודת קונסטרקטור
        self.list1=["Heart","Club","Diamond","Spade"]
        self.list2=["1","2","3","4","5","6","7","8","9","Prince","Queen","King","Ace"]
        self.list3=[]
        for i in self.list1:
            for x in self.list2:
                self.list3.append(Card(i,x))
    def Shuflle(self):                   #מתודת ערבוב של קלפים
        if len(self.list3)<52:
            print("You can't shuflle the deck after game began.")
            return
        shuffle(self.list3)
    def dealOne(self):                  #שולפת קלף מראש החפיסה
        return self.list3.pop()
    def newGame(self):                 #יוצרת חפיסה חדשה ומערבבת
        self.__init__()
        shuffle(self.list3)
    def show(self):                   #מדפיסה את רשימת הקלפים
        for i in self.list3:
            print(f'Card Details: {i.Suit} , {i.Value}' , end=' ')
