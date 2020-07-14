enum = int(input("Enter a number: "))
sum = 0
max = 0
min = 0
list = []
for i in range(0, enum):
    list.append(int(input("Enter a new number: ")))
max = list[0]
min = list[0]
print(list)
for i in list:
    sum += i
    if max < i:
        max = i
    if min > i:
        min = i
print("The avg of list: " + str(sum / enum) + "The min of list: " + str(min) + "The max of list: " + str(max))
