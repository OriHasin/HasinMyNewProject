count = 0
avg = 0
for i in range(0, 10):
    grade = int(input("Enter grade you received: "))
    if grade < 0 or grade > 100:
        count += 1
        if count == 5:
            break
        continue
    avg += grade
else:
    print("The average of grades: " + str(avg / 10))
