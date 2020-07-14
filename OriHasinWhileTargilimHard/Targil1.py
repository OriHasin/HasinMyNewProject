num = int(input("Enter the first num: "))
min = num
while num != 0:
    if num > 0:
        if num < min:
            min = num
    num = int(input("Enter the first num: "))
print("The min num is: " + str(min))
