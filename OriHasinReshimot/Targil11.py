list2=[1,1]
sum=2
for i in range(2,10):
    list2.append(sum)
    sum+=list2[i]
print(list2)