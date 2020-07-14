sum = 0
count = 0
for i in range(1, 7):
    num = int(input("Enter the first number: "))
    if num % 2 == 0:
        sum += num
        count += 1
print("The average of num: " + str(sum / count))
