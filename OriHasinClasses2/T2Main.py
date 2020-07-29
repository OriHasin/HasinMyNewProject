from OriHasinClasses2.T2Class import *
if __name__=='__main__':
    seats=int(input("Enter number of seats: "))
    Bus1=Bus(seats)
    num=int(input("Enter a number you want to do on the bus . 1 - get on passenger on the bus , 2 - get off passenger from the bus , 0 - stop program: "))
    while num!=0:
        name=input("Enter a passenger name: ")
        if num==1:
            Bus1.getOn(name)
        if num==2:
            Bus1.getOff(name)
        num = int(input("Enter a number you want to do on the bus . 1 - get on passenger on the bus , 2 - get off passenger from the bus , 0 - stop program: "))
    print(Bus1.__str__())
