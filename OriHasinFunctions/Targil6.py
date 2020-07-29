def printnumbers(num1,num2):
    for i in range(num1,num2+1):
        print (str(i)+" ",end='')
if __name__=='__main__':
    num1=int(input("Enter a smaller number: "))
    num2=int(input("Enter a bigger number: "))
    printnumbers(num1,num2)