list=[int(input("Enter a new digit: ")) for i in range(10)]
for i in range(10):
    print("The number"+str(list[i])+"appeared: "+str(list.count(list[i])))
