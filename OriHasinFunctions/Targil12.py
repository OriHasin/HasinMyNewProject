def randominlistfunction(list):
    from random import randint
    list=[randint(1,100) for i in range(20)]
    return list
def numinlist(num,list):
    return list.count(num)
def maxinlist(list):
    maxnum=max(list)
    return list.index(maxnum)
if __name__=='__main__':
    list=[]
    list=randominlistfunction(list)
    print(list)
    num=int(input("Enter a new number: "))
    print(numinlist(num,list))
    print(maxinlist(list))
