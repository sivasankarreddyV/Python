  #single inheritance
  #person is base or super or parent
  #student is derived or subclass or child class


class person:  
    def _init_(self,name,age):
     self.name=name
     self.age=age
    def display(self):
     print("Name is:",self.name)
     print("Age is:",self.age)

class student(person):
    def _init_(self,name,age,sid,course):
     super()._init_(name,age)
     self.student_id=sid
     self.major=course
    def display(self):
     super().display()
     print("Student id is:",self.student_id)
     print("Student Main course is:",self.major)

s1=student("Siva",22,143,"Python")
s1.display()()
