from GameCards_OriHasin.DeckOfCards import DeckOfCards
from GameCards_OriHasin.Card import Card
class Player:
    #מחלקה המגדירה קלף במשחק
    #Name,Amount, list1 -רשימה של קלפי השחקן, list2 = חפיסת קלפים המתקבלת ליצירת חבילת קלפים אישית לשחקן

    def __init__(self,Name,Amount,NumOfCards=5):#מתודת קונסטרקטור
        self.Name=Name
        if self.Name == '': #בודק שלא מכניסים שם ריק
            raise ValueError("Name can't be empty , Please enter a name of player ")
        self.Amount=Amount
        self.NumOfCards=NumOfCards
        if self.NumOfCards<=0:
            raise ValueError("Player can't be with '0' or negative number of cards")
        self.list1=[]

    def __repr__(self):  # מתודה המדפיסה פרטי שחקן
            return (f'Player Details: {self.Name} , {self.Amount} , {self.list1}')

    def setHand(self,Deck1): #מתודה היוצרת חבילת קלפים
        if type(Deck1) != DeckOfCards:#בדיקה שהאובייקט המתקבל מסוג חפיסת קלפים
            raise ValueError("Send only DeckOfCards.")
        for i in range(self.NumOfCards):
            self.list1.append(Deck1.dealOne())

    def getCard(self):#מתודה המושכת קלף מהשחקן
        if len(self.list1)==0:#בדיקה שהפונקציה לא מתבצעת על חבילת קלפים ריקה
            raise ValueError("You can't get card , the deck is empty")
        return self.list1.pop()

    def addCard(self,card): #מתודה המוסיפה קלף לשחקן
        if type(card)!=Card:#בדיקה שהאובייקט המתקבל מסוג קלף
            raise ValueError("Send only a Card")
        self.list1.append(card)

    def reduceAmount(self,amount): #מתודה המורידה סכום לשחקן
        if type(amount)!=int:#בדיקה שהפרמטר המתקבל מסוג מספר שלם
            raise ValueError("Send a int number")
        if amount<=0:#בדיקה שהפרמטר המתקבל חיובי בלבד
            raise ValueError("Send only a positive number")
        if self.Amount-amount<0:#בדיקה שלא מתווצר סכום אישי שלילי
            self.Amount=0
            print("The amount of player is '0'")
            return
        self.Amount-=amount

    def addAmount(self,amount): #מתודה המוסיפה סכום לשחקן
        if type(amount)!=int:#בדיקה שהערך המתקבל מסוג מספר שלם
            raise ValueError("Send a int number")
        if amount<=0:#בדיקה שהערך המתקבל חיובי
            raise ValueError("Send only a positive number")
        self.Amount+=amount