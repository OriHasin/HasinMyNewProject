class Card:
    # מחלקה היוצרת קלף במשחק
    #Suit,Value
        def __init__(self,Suit,Value): #מתודת קונסטרקטור
            self.Suit=Suit
            self.Value=Value
        def __str__(self): #מתודת הדפסה
            return f'Card Details: {self.Suit} : {self.Value}'#

