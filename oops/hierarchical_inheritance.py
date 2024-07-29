#Heirarchcal inheritance (multiple derived classes from one base class)
#person is base or super or parent
#student is derived or subclass or child class
#teacher is a derived or subclass or child class
class person:  
    def __init__(self,name,age):
     self.name=name
     self.age=age
    def display(self):
     print("Name is:",self.name)
     print("Age is:",self.age)

class student(person):
    def __init__(self,name,age,sid,course):
     super().__init__(name,age)
     self.student_id=sid
     self.major=course
    def display(self):
     super().display()
     print("Student id is:",self.student_id)
     print("Student Main course is:",self.major)

class teacher(person):
    def __init__(self,name,age,eid,subject,salary):
     super().__init__(name,age)
     self.employee_id=eid
     self.subject=subject
     self.salary=salary
    def display(self):
     super().display()
     print("Employee id is:",self.employee_id)
     print("Subjet is:",self.subject)
     print("Salary is:",self.salary)
    
s1=student("Siva",23,840,"Python")
s1.display()

t1=teacher("Reddy",49,420,"Python",100000)
t1.display()

