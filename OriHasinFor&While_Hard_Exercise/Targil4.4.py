from random import *

i = 0
Rnum = randint(1, 100)
max = 100
min = 1
print("My guess is: " + str(Rnum))
what = input("Enter high/low/good: ")
while what != 'good':
    if what == 'high':
        max = Rnum
        Rnum = randint(min, max)
    else:
        min = Rnum
        Rnum = randint(min, max)
    i += 1
    print("My guess is: " + str(Rnum))
    what = input("Enter high/low/good: ")
print("The number of trying the pc did: " + str(i))
