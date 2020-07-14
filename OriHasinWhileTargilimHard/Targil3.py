num = int(input("Enter choose of num: "))
i = 1
serial = i
max = num
while (i < 7):
    if num > max:
        max = num
        serial = i
    num = int(input("Enter choose of num: "))
    i += 1
if max > num:
    print("The serial max number: " + str(serial))
else:
    max = num
    serial = i
    print("The serial max number: " + str(serial))
