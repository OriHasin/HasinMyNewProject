class StudentInClass:
    #Id,Name,Adress,Grade
    def ifpass(self):
        if self.Grade<70:
            return False
        else:
            return True
if __name__=='__main__':
    student=StudentInClass()
    student.Id=input("Enter your current id: ")
    student.Name=input("Enter your current name: ")
    student.Adress=input("Enter your current adress: ")
    student.Grade=int(input("Enter yout current grade: "))
    if student.ifpass()==False:
        print("You Failed")
    else:
        print("You Passed")