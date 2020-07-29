def FloatToInt(num1):
    num2=int(num1)
    sum = 1 - (num1 - num2)
    if(num1-num2>=0.5):
        num1+=sum
        num1=int(num1)
    else:
        num1=int(num1)
    return num1
if __name__=='__main__':
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    print(FloatToInt(num1)+FloatToInt(num2))
    