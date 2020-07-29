def OpositeNum(num1):
    num2=""
    while num1!=0:
        num2+=str(num1%10)
        num1=num1//10
    return int(num2)
if __name__=='__main__':
    num1=int(input("Enter a new number: "))
    print(OpositeNum(num1)+num1)
