dic={}
num=int(input("Enter a new number: "))
for i in range(1,num+1):
    dic.update({i:i*i})
print(dic)
del dic[3]
print(dic)