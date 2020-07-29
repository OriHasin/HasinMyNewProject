class Student:
    #Name,Adress,Age,List
    def __init__(self):
        self.List=[]
    def details(self):
        print(f'{self.Name} {self.Adress} {self.Age} {self.List} ')
    def UpdateAge(self,age):
        self.Age=age
    def StudentAge(self):
        return self.Age
    def AddGrade(self,grade):
        if len(self.List)>=5:
            return False
        else:
            self.List.append(grade)
            return True
    def AvgStudent(self):
        sum=0
        for i in self.List:
            sum+=i
        return sum/len(self.List)
    def StudentList(self):
        return self.List
if __name__=='__main__':
    student=Student()
    student.Name=input("Enter your current name: ")
    student.Adress=input("Enter your current adress: ")
    student.UpdateAge(int(input("Enter your current age: ")))
    for i in range(5):
        student.AddGrade(int(input("Enter a new grage: ")))
    student.details()
    if student.StudentAge()<20:
        print("Very Young")
    if student.StudentAge()>=20 and student.StudentAge()<=30:
        print("Young")
    if student.StudentAge()>=31:
        print("Mature")
    print(student.StudentList())


