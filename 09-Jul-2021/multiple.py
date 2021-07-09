class cal1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self,a,b):
        return a+b
class cal2:
    def subtract(self,a,b):
        return a-b
class cal3:
    def multiply(self,a,b):
        return a*b
class calculate(cal1,cal2,cal3):
    def display(self,a,b):
        print("\nThe sum of two numbers is",c1.sum(a,b))
        print("\nThe diiference of two numbers is",c1.subtract(a,b))
        print("\nThe multiplication of two numbers is",c1.multiply(a,b))
class cal4(calculate):
    def divide(self,a,b):
        print("\n Division of two numbers is",round(a/b))
        c1.display(a,b)
a=int(input("Enter a"))
b=int(input("Enter b"))
c1=cal4(a,b)
c1.divide(a,b)




