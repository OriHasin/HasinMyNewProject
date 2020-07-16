num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
Space = num1 - num2
if Space < 0:
    Space = Space * (-1)
    print("The answer is: " + str(Space))
else:
    print("The answer is: " + str(Space))
print("Hey")