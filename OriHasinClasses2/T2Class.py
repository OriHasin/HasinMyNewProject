class Bus:
    #List,NumOfPassengers
    def __init__(self,num):
        self.List=['Free' for i in range(num)]
        self.NumOfPassengers=0
    def getOn(self,name):
        for i in range(len(self.List)):
            if self.List[i]=='Free':
                self.List[i]=name
                self.NumOfPassengers+=1
                break
        else:
            print("The passenger: "+name+" "+" don't get on to the bus")
    def getOff(self,name):
        for i in range(len(self.List)):
            if self.List[i]==name:
                self.List[i]='Free'
                self.NumOfPassengers-=1
                break
        else:
            print("The passenger: "+name+" "+"don't available on the bus")
    def __str__(self):
        return f'The List of seats: {self.List}'
