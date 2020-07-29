def powfunction(num1,num2):
    sum=1
    for i in range(num2):
        sum*=num1
    print(sum)
if __name__=='__main__':
    num1=int(input("Enter a new number: "))
    num2=int(input("Enter a new number: "))
    powfunction(num1,num2)
