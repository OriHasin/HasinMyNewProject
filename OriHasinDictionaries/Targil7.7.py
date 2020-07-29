dic1={1:10,2:20,3:30,4:40,5:50,6:60,7:70,8:80,9:40,10:80}
dic2={}
t=1
values=sorted(set(dic1.values()))
values=list(values)
for i in range(len(values)):
   dic2.update({t:values[i]})
   t+=1
print(dic2)