num = int(input("Enter number: "))
if num // 100 != 0 and num // 1000 == 0:
    digit1 = num % 10
    digit2 = (num // 10) % 10
    digit3 = num // 100
    sum = digit1 + digit2 + digit3
    print("The sum of his digits is: " + str(sum))
else:
    print("Invailed")
