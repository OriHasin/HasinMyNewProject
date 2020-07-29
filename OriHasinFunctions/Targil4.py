def sumofdigits(num):
    sum=0
    for i in range (1,num+1):
        sum+=i
    return sum

if __name__=='__main__':
    num=int(input("Enter a new number: "))
    print(sumofdigits(num))



