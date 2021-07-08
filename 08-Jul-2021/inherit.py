class student:
    def get(self):
        self.name=input("Name:")
        self.gender=input("Gender:")
        #return self.name,self.gender
class test(student):
    def marks(self):
        self.stuclas=input("class:")
        self.mark1=int(input("Mark1:"))
        self.mark2=int(input("Mark2:"))
        print("\nFrom student class,Name:",self.name)
        print("\nFrom student class,Gender:",self.gender)
        print("\nFrom test class,get class:",m.stuclas)
        
class marks(test):
    def display(self):
        self.age=input("Age:")
        self.tot=self.mark1+self.mark2
        print("\nFrom test class, MARK1:",self.mark1,"MARK2:",m.mark2)
        print("\nFrom test class calculate marks,Total:",self.tot)

class percent(marks):
    def cal(self):
        self.per=round((self.tot/200)*100)
        print("\n The obtained percentage is",self.per)
        return self.per
m=percent()
print("Enter the name,gender")
m.get()
print("Enter the class and marks")
m.marks()
print("\nEnter the age")
m.display()
print("\nDisplaying the percentage")
m.cal()