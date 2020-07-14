num = int(input("Enter the first number: "))
while num != 0:
    firstd = num % 10
    num = num // 10
print("The first digit is: " + str(firstd))
