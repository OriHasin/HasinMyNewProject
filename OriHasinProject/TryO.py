try:
    num=int(input("Enter a new kaki: "))
except ValueError:
    raise ValueError("Enter a int number")
else:
    print("Good job Ori Hasin")