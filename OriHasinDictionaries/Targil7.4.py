keys=int(input("Enter a new number: "))
dic1={}
for i in range(1,keys+1):
    dic1.update({i:i*i})
print(dic1)