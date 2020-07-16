str1=input("Enter a new string: ")
list=[]
for i in str1:
    if i not in list:
        list.append(i)
print(list)
