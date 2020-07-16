list=[i for i in range(1,11)]
list2=[]
for i in list:
    if i%3==0:
        list2.append(i)
        list.remove(i)
print(list)
print(list2)
