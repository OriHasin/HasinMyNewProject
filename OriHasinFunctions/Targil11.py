def newlistfunction(list):
    for i in range(2,41,2):
        list.append(i)
    return list
if __name__=='__main__':
    list=[]
    list=newlistfunction(list)
    print(list)