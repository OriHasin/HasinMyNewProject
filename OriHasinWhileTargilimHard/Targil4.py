num = int(input("Enter a new number: "))
nnum = num
count = 0
stnum = str()
while nnum != 0:
    count += 1
    nnum = nnum // 10
for i in range(0, count):
    stnum = stnum + str(num % 10)
    num = num // 10
print("The new number is: " + stnum + " " + "The multiply is: " + str(int(stnum) * 2))
