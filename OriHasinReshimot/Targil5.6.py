list=[i for i in range(1,11)]
list1=list[7:]
print(list1)
print(list[::-1])
print(list[::2])
list2=list[::2]
print(list2)
num1=int(input("Enter a new number: "))
num2=int(input("Enter a new number: "))
num3=int(input("Enter a new number: "))
list[4:6]=[num1,num2]
list.append(num3)
print(list)
list3=[list[i]*2 for i in range(10)]
print(list3)
list4=[list[0],list[-2]]
print(list4)

