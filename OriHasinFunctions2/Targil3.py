def NewString(str1):
    str2=""
    str2=str1[0]+str1[-1]
    for i in range(len(str1)):
        print(str2)
if __name__=="__main__":
    str1=input("Enter a new string: ")
    NewString(str1)