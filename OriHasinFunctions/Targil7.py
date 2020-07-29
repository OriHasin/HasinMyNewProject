def minfunction(num1,num2):
    if num1>=num2:
        return num2
    else:
        return num1
def maxfunction(num1,num2):
    if num2>=num1:
        return num2
    else:
        return num1
from OriHasinFunctions.Targil6 import *
if __name__=='__main__':
    num1=int(input("Enter a new number: "))
    num2=int(input("Enter again new number: "))
    num3=minfunction(num1,num2)
    num4=maxfunction(num1,num2)
    printnumbers(num3,num4)