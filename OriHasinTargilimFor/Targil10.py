num = int(input("Enter a new number: "))
i = 0
while num != 0:
    if num % 7 == 0 or num % 3 == 0:
        i += 1
    num = int(input("Enter a new number: "))
print("The num of divided: " + str(i))
