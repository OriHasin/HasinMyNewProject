num = int(input("Enter a new num: "))
for i in range(num, 0, -1):
    for x in range(i, 0, -1):
        print("*", end=' ')
    print("")
