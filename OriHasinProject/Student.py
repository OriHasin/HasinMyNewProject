class Student:
    #ID,Name,List1
    def __init__(self,ID,Name):
        self.ID=ID
        self.Name=Name
        self.dict1={}
    def add_grade(self,NameCourse,Grade):
        self.dict1[NameCourse]=Grade
    def __repr__(self):
        return f'ID: {self.ID} ,Name: {self.Name} ,Grades: {self.dict1} '
    def calc_factor(self,NameCourse,Factor):
        self.dict1[NameCourse]+=(self.dict1[NameCourse]*(Factor/100))
        if self.dict1[NameCourse]>100:
            self.dict1[NameCourse]=100
    def average(self):
        sum=0
        for i in self.dict1:
            sum+=self.dict1[i]
        return sum/len(self.dict1)
