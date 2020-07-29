from OriHasinProject.Student import Student
class Course:
    #ID,Name,Dict1,List1,MaxStudents
    def __init__(self,ID,Name,Dict1,MaxStudents):
        self.ID=ID
        self.Name=Name
        self.Dict1=Dict1
        self.List1=[]
        self.MaxStudents=MaxStudents
    def __repr__(self):
        return f'Name: {self.Name} ,ID: {self.ID} ,Topics: {self.Dict1} ,Students: {self.List1} ,Max students in course: {self.MaxStudents}'
    def add_student(self,Student):
        while len(self.List1)<self.MaxStudents:
            self.List1.append(Student)
            return True
        return False
    def add_factor(self,NameCourse,Factor):
        for i in self.List1:
            i.calc_factor(NameCourse,Factor)
    def del_student(self,ID):
        for i in self.List1:
            if i.ID==ID:
                self.List1.remove(i)
    def calc_avg(self):
        sum=0
        for i in self.List1:
            sum+=i.calc_average()
        return sum/len(self.List1)







