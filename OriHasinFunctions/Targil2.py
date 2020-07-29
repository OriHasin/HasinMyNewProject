def if3(num):
    num=str(num)
    if len(num)==3:
        print("It is 3 digits")
    else:
        print("It isnt 3 digits")
if __name__=='__main__':
    num=int(input("Enter a new number: "))
    if3(num)