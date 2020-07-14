num = int(input("Enter number: "))
count = True
for i in range(2, 4):
    if num % i == 0:
        count = False
        break
if count == True:
    print("Good number")
else:
    print("Not Good")
