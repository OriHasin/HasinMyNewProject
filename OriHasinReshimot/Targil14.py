num=int(input("Enter a new number: "))
list=[]
for i in range (1,num//2+1):
    if num%i==0:
        list.append(i)
print(list)