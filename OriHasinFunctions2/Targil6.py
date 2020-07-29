def IfDiscount(age,city):
    if age<=10:
        return 1
    if age>10 and age<=18:
        return 0.25
    if age>10 and age<=18 and city=='jerusalem':
        return 0.35
    if age>18 and age<=60 and city=='jerusalem':
        return 0.1
    if age>60:
        return 0.5
    else:
        return 0
def Price(price,discount):
     sum=0
     sum=price*discount
     return price-sum
if __name__=='__main__':
    price=int(input("Enter the current price: "))
    age=int(input("Enter the current age: "))
    city=input("Enter the current city: ")
    discount=IfDiscount(age,city)
    print(f'The new price is: {Price(price,discount)}')