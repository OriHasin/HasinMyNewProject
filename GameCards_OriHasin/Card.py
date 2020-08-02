class Card:
    # מחלקה היוצרת קלף במשחק
    #Suit,Value , list1 = רשימה של סוגי קלפים , list2 = רשימה של ערכי קלפים
        def __init__(self,Suit,Value): #מתודת קונסטרקטור
            self.Suit=Suit
            self.Value=Value
        def __repr__(self): #מתודת הדפסה
            return f'Card Details: {self.Suit} : {self.Value}'
        def __gt__(self, other): #מתודה המשווה בין ערכים
            self.list1=["♦","♠","♥","♣"]
            self.list2=["2","3","4","5","6","7","8","9","10","Prince","Queen","King","Ace"]
            for i in range(len(self.list1)): #מגדיר מיקום של הסוג
                if self.Suit==self.list1[i]:
                    indexS=i
            for i in range(len(self.list1)): #מגדיר מיקום של הסוג באובייקט השני
                if other.Suit==self.list1[i]:
                    indexSO=i
            for i in range(len(self.list2)): #מגדיר מיקום של הערך
                if self.Value==self.list2[i]:
                    indexV=i
            for i in range(len(self.list2)): #מגדיר מיקום של הערך באובייקט השני
                if other.Value==self.list2[i]:
                    indexOV=i
            if indexV>indexOV:
                return True
            elif indexV==indexOV:
                if indexS>indexSO:
                    return True
                else:
                    return False
            else:
                return False






