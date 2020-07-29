class Course:
    #Cnum,Cname,NRStudents,NMStrudents
    def details(self):
        return f'{self.Cnum} {self.Cname} {self.NRStudents} {self.NMStudents}'
    def freechair(self):
        return self.NMStudents-self.NRStudents

if __name__=='__main__':
    course1=Course()
    course1.Cnum=int(input("Enter a course number: "))
    course1.Cname=input("Enter name of course: ")
    course1.NRStudents=int(input("Enter number of students: "))
    course1.NMStudents=int(input("Enter number maximun students: "))
    print(course1.details())
    print(course1.freechair())
