dic1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic2={}
keys=dic1.values()
keys=list(keys)
values=dic1.keys()
values=list(values)
for i in range(len(keys)):
    dic2.update({keys[i]:values[i]})
print(dic2)
