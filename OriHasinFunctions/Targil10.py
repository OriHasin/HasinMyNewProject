def passfunction(grade):
    if grade>=70 and grade<=100:
        return True
    else:
        return False
if __name__=='__main__':
    for i in range(5):
        grade=int(input("Enter a new grade: "))
        if passfunction(grade)==True:
            print("You passed the test")
        else:
            print("Sorry,you dont passed ")