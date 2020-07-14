from random import *

Rnum = randint(1, 9)
num = int(input("Enter choose of number: "))
while num != Rnum:
    num = int(input("Enter again new number: "))
print("Good choice, you guessed the number!")
