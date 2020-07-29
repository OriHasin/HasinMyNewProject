from OriHasinProject.Student import Student
from OriHasinProject.Course import Course
list1=[]
dict1={}
id=int(input("Enter a course id: "))
name=input("Enter name of course: ")
MaxStudents=int(input("Enter a maximun students: "))
subject=input("Enter a new subject, for stopping enter null: ")
teacher=input("Enter a new teacher: ")
while subject!='null':
    dict1[subject]=teacher #יוצרים מילון עם נושא:מרצה
    subject = input("Enter a new subject, for stopping enter null: ")
    teacher = input("Enter a new teacher: ")
course1=Course(id,name,dict1,MaxStudents)
idstudent=int(input("Enter a student id,for stopping enter '0': "))
namestudent=input("Enter a student name: ")
while idstudent!=0 and len(course1.List1)<MaxStudents: #כל עוד יש מקום
    student1=Student(idstudent,namestudent)
    for i in dict1:
        student1.add_grade(i,int(input(f'Enter a new grade for this subject{i}:'))) #מפעיל פונקצית הוספת ציון למילון לכל נושא
    course1.add_student(student1)
    idstudent = int(input("Enter a student id,for stopping enter '0': "))
    namestudent = input("Enter a student name: ")
factorsubject=input("Enter a Factor subject :")
factor=float(input("Enter a factor amount: "))
course1.add_factor(factorsubject,factor)#הוספת פקטור לכל סטודנט
min=100
index=0
for i in list1:
    if i.average()<min:
        min=i.average()
        index=i
for i in list1: #מחיקת ערך ממוצע מינימלי
    if i.average()==index.average():
        list1.remove(i)
print(course1.__repr__())

