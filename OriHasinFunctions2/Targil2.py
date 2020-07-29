def NewString(str1):
    str1=str1[::-1]
    return str1
if __name__=='__main__':
    str=input("Enter a new string: ")
    for i in range(3):
        print(NewString(str),end='')