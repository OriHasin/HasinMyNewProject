list1=[input("Enter a new name: ") for i in range(5)]
list2=[int(input("Enter a new grade: ")) for i in range(5)]
dic1={}
list3=[]
for i in range(5):
    dic1.update({list1[i]:list2[i]})
avg=sum(dic1.values())/5
print(avg)
for i in dic1:
    if dic1[i]>avg:
        list3.append(i)
print(list3)