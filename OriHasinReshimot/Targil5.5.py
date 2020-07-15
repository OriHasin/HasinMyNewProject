count=0
list=[]
grade=int(input("Enter yout new grade: "))
while grade!=0:
    list.append(grade)
    grade=int(input("Enter the next grade: "))
for i in list:
    if i<60:
        count+=1
print("The number of fail grades:"+str(count)+"\nThe number of success grades: "+str(len(list)-count))
