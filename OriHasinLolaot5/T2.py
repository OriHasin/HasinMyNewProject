num = int(input("Enter a new number: "))
for i in range(0, num):
    for x in range(0, i + 1):
        print("*", end='')
    print("")
