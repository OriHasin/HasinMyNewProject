class Animal:
    #Name,Hungry,Energy
    def __init__(self,Name):
        self.Name=Name
        self.Hungry=5
        self.Energy=5
    def __str__(self):
        return f'The name: {self.Name} The amount of hungry: {self.Hungry} The amount of energy: {self.Energy}'
    def Eat(self,food):
        if food<50:
            print("The animal need minimum 50 grams to eat")
            return
        if food>=50 and food<100:
            self.Hungry=self.Hungry-1
            self.Energy=self.Energy-0.5
            if self.Hungry <= 0:
                print("The animal ate a lot , she stopped")
                self.Energy = self.Energy + (0 - self.Hungry) * 0.5
                self.Hungry = 0
                return
            if self.Energy <= 0:
                print("The animal had no energy")
                self.Energy = 0
                return
            print("The animal ate 50 grams")
            return
        if food>=100:
            amount=food//100
            if food%100==50:
                self.Hungry=self.Hungry-1
                self.Energy=self.Energy-0.5
            while amount!=0:
                self.Hungry=self.Hungry-2
                self.Energy=self.Energy-1
                if self.Hungry<=0:
                    print("The animal ate a lot , she stopped")
                    self.Energy=self.Energy+(0-self.Hungry)*0.5
                    self.Hungry=0
                    break
                if self.Energy<=0:
                    print("The animal had no energy")
                    self.Energy=0
                    break
                amount=amount-1
        return
    def Play(self,Time):
        sum=Time//10
        if sum==0:
            print("The animal need minimum 10 minutes")
            return
        while sum!=0:
            self.Energy=self.Energy-2
            self.Hungry=self.Hungry+2
            if self.Energy<=0:
                print("The animal is tired")
                self.Hungry=self.Hungry-(0-self.Energy)
                self.Energy=0
                break
            if self.Hungry>=10:
                print("The animal is hungry")
                self.Hungry=10
                break
            sum=sum-1
        return
    def Rest(self,RTime):
        if RTime<10:
            print("The animal need minimum 10 minutes to rest")
            return
        RSum=RTime//10
        while RSum!=0:
            self.Energy=self.Energy+0.5
            self.Hungry=self.Hungry+0.333
            if self.Energy>=10:
                print("The animal finish to rest , she want to play")
                self.Energy=10
                return
            if self.Hungry>=10:
                print("The animal is hungry , she want to eat")
                self.Hungry=10
                self.Energy=self.Energy+RSum*0.5
                return
            RSum=RSum-1
        return
if __name__=='__main__':
    name=input("Enter name of animal: ")
    Animal1=Animal(name)
    num=int(input("Enter a number you want the animal do : 1 - eat , 2 - play , 3 - rest , 0 - stop program: "))
    while(num!=0):
        if num==1:
            food=int(input("Enter a food amount: "))
            Animal1.Eat(food)
            print(Animal1.__str__())
        if num==2:
            Time=int(input("Enter a play time: "))
            Animal1.Play(Time)
            print(Animal1.__str__())
        if num==3:
            RTime=int(input("Enter a rest time: "))
            Animal1.Rest(RTime)
            print(Animal1.__str__())
        num = int(input("Enter a number you want the animal do : 1 - eat , 2 - play , 3 - rest , 0 - stop program: "))











