class Person:
    #name,age,NumOfChildren
    def __init__(self,name,age,NumOfChildren):
        self.name=name
        self.age=age
        self.NumOfChildren=NumOfChildren
    def __str__(self):
        return f'The name is: {self.name},The age is: {self.age},The number of children is: {self.NumOfChildren}'
    def hasChildren(self):
        if self.NumOfChildren>0:
            return True
        else:
            return False
    def ageGroup(self):
        if self.age>=0 and self.age<=18:
            return 'Child'
        if self.age>=19 and self.age<=60:
            return 'Adult'
        if self.age>=61 and self.age<=120:
            return 'Senior'
if __name__=='__main__':
    name=input("Enter your current name: ")
    age=int(input("Enter your current age: "))
    NumOfChildren=int(input("Enter number of children: "))
    Person1=Person(name,age,NumOfChildren)
    print(Person1.__str__())
    if Person1.hasChildren()==True:
        print("He have a children")
    elif Person1.hasChildren()==False:
        print("He dont have children")
    print(Person1.ageGroup())
