num = int(input("Input a positive number: "))
num2 = int(input("Input a positive number: "))
divi = 1
mudu = 0
while num2 > num:
    num2 = int(input("Input a little number: "))
nnum = num2
while num2 + nnum <= num:
    divi += 1
    num2 += nnum
mudu = num - (nnum * divi)
print("The divided is: " + str(divi) + " " + "The mudulo is: " + str(mudu))
