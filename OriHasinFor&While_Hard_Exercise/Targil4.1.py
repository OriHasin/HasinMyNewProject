num1 = int(input("Enter num: "))
num2 = int(input("Enter num2: "))
if num1 >= num2:
    for num2 in range(num2 + 1, num1):
        if num2 % 2 == 0:
            print(num2)
        else:
            continue  # לא חובה

else:
    for num1 in range(num1 + 1, num2):
        if num1 % 2 == 0:
            print(num1)
        else:
            continue  # לא חובה
