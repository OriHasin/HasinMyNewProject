from random import *
def NewList(n):
    list=[randint(10,1000) for i in range(n)]
    return list
def OpositeList(list):
    from OriHasinFunctions.Targil9 import OpositeNum
    list2=[]
    for i in list:
        list2.append(OpositeNum(i))
    return list2
if __name__=='__main__':
    list=NewList(int(input("Enter a new number: ")))
    print(list)
    list=OpositeList(list)
    print(list)