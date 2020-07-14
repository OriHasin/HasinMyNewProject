age = int(input("Enter age: "))
if age >= 0 and age <= 18:
    print("Child")
elif age > 18 and age <= 60:
    print("Adult")
elif age > 60 and age <= 120:
    print("Senior")
