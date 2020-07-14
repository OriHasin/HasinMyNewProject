string = input("Enter a sentence: ")
print("The length is: " + str(len(string)))
print("The string is: " + string[2:6])
nstring = string.split(" ")
print("The first word is: " + nstring[0] * 3)
for i in nstring:
    print(i.capitalize())
