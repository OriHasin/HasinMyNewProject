day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
count = 0
if day < 1 or day > 31:
    print("The day is incorrect")
    count += 1
elif month < 1 or month > 12:
    print("The month is incorrect")
    count += 1
elif year < 1950 or year > 2020:
    print("The year is incorrect")
    count += 1
if count == 0:
    print("The date is: " + str(day) + "/" + str(month) + "/" + str(year // 10 % 10) + str(year % 10))
