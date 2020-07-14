num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num % 2 == 0 and num2 % 2 == 0:
    print("Good number,The sum: " + str(num + num2))
else:
    print("isnt good number,Mul: " + str(num * num2))
