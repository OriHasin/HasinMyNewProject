def NewString(str1):
    str2=""
    for i in range(len(str1)):
        if str1[i]=='A' or str1[i]=='a':
            continue
        else:
            str2+=str1[i]
    print(str2)
if __name__=='__main__':
    str2=input("Enter a new string: ")
    NewString(str2)
