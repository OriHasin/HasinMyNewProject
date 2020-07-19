dic1={1:10}
dic2={2:20}
dic3={3:30}
dic4={}
list=[dic1,dic2,dic3]
for i in list:
    dic4.update(i)
print(list)