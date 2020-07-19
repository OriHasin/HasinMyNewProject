num=int(input("Enter a number now: "))
list=[1,1]
for i in range(2,num):
    list.append(list[i-1]+list[i-2])
print(list)

