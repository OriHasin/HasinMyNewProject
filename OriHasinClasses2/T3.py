from random import *
class Loto:
    #UP,LOW,List,Amount
    def RandomToList(self):
        self.List=[randint(self.LOW,self.UP) for i in range(6)]
    def InputAmount(self):
        self.Amount=int(input("Enter a maximun amount: "))
    def __init__(self):
        self.UP=45
        self.LOW=1
        self.RandomToList()
        self.InputAmount()
    def PrintList(self):
        print(self.List)
    def NumInList(self,num):
        for i in self.List:
            if i==num:
                return True
        return False
    def NumOfGuess(self,num):
        if num<=1:
            return 0
        if num>1 and num<=5:
            return (self.Amount*num)/6
        if num==6:
            return self.Amount
if __name__=='__main__':
    Loto1=Loto()
    count=0
    Loto1.PrintList()
    for i in range(6):
        num=int(input("Enter a new number: "))
        if num<1 or num>45:
            print("The num isn't good")
            count=0
            break
        if Loto1.NumInList(num)== True:
            count+=1
    print("The amount you get: "+str(Loto1.NumOfGuess(count)))


