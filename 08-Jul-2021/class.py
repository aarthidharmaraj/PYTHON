class student:
    college="XYZ college"
    def __init__(self,names,course,rollno):
        self.names=names
        self.rollno=rollno
        self.course=course
    @classmethod
    def disp(cls,name,course,rollno):
        return name,course,rollno
    def calcu(self,marks):
        print("The name of college is",student.college)
        self.perce=(marks/500)*100
        return self.perce
    @staticmethod
    def add(cs,m3,envi,ae,pe):
            tot=cs+m3+envi+ae+pe
            print("\nThe sum of marks",tot)
    
print("\nenter the name,rollno,course")
name=input()
rollno=int(input())
course=input()
s1=student(name,rollno,course)
s1.disp(name,rollno,course)
print("The details of the student are\nName:",name,"Rollno:",rollno,"Course:",course)
cs,m3,envi,ae,pe=98,76,89,67,87
s1.add(cs,m3,envi,ae,pe)
print("\nEnter the total marks")
marks=int(input())
s1.calcu(marks)
print("The percentage is",round(s1.perce))