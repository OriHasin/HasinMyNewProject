def ageinrange(age):
    if age>0 and age<=18:
        return 'Child'
    if age>18 and age<=60:
        return 'Adult'
    if age>60 and age<=120:
        return 'Senior'
if __name__=='__main__':
    for i in range(5):
        age=int(input("Enter your current age: "))
        print(ageinrange(age))
