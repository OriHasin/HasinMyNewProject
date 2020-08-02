from GameCards_OriHasin.DeckOfCards import DeckOfCards
class Player:
    #מחלקה המגדירה קלף במשחק
    #Name,Amount, list1 -רשימה של קלפי השחקן, list2 = חפיסת קלפים המתקבלת ליצירת חבילת קלפים אישית לשחקן

    def __init__(self,Name,Amount,NumOfCards=5): #מתודת קונסטרקטור
        self.Name=Name
        self.Amount=Amount
        self.NumOfCards=NumOfCards
        self.list1=[]
    def __repr__(self):  # מתודה המדפיסה פרטי שחקן
            return (f'Player Details: {self.Name} , {self.Amount} , {self.list1}')

    def setHand(self,Deck1): #מתודה היוצרת חבילת קלפים
        for i in range(self.NumOfCards):
            self.list1.append(Deck1.dealOne())

    def getCard(self): #מתודה המושכת קלף מהשחקן
        return self.list1.pop()

    def addCard(self,card): #מתודה המוסיפה קלף לשחקן
        self.list1.append(card)

    def reduceAmount(self,amount): #מתודה המורידה סכום לשחקן
        self.Amount-=amount

    def addAmount(self,amount): #מתודה המוסיפה סכום לשחקן
        self.Amount+=amount