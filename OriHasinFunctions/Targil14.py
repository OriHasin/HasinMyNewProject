def ListGrade(NumS):
    list=[int(input("Enter a new grade: ")) for i in range(NumS)]
    return list
def AvgGrade(list):
    sum=0
    for i in list:
        sum+=i
    return sum/len(list)
if __name__=='__main__':
    NumS=int(input("Enter a number students: "))
    list=ListGrade(NumS)
    avg=AvgGrade(list)
    print(f'The list is {list} The Average is {avg}')
    