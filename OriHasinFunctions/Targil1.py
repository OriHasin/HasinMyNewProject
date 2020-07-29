def sum(num):
    sum=0
    while num!=0:
        sum+=num%10
        num=num//10
    return sum
if __name__=='__main__':
    num=int(input("Enter a new number: "))
    sum=sum(num)
    print("The sum of digits: "+str(sum))
     