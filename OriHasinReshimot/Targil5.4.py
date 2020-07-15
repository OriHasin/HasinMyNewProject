list=[input("Enter a new number: ") for i in range(10)]
list2=[input("Enter again new number: ") for i in range(10)]
list+=list2
print("The new list is: "+str(list))
print("The length of list: "+ str(len(list)))