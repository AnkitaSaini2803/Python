'''21/1/2025
Super() Keyword in python is used to refer parent class
sometimes,you may want to use the parent class methods in child class...
there you use super keyword
'''
class Parent:
    def parent_method(self):
        print("You call parent method")
class child(Parent):
    
    def child_method(self):
        print("This is Child method inside child class")
        super().parent_method() 

    def parent_method(self):
       print("This is Ankita")
       super().parent_method() 

object=child()
object.child_method()  
object.parent_method() 




class Employee:
    def employee(self,name,id):
        self.name=name
        self.id=id
class Employee1(Employee):
    def employee1(self,name,id,lang):
        # self.name=name
        # self.id=id
        super().employee(name,id)
        self.skills=lang

emp=Employee1()
emp.employee1('Ankita',14,'Master In Python Programming')
print(emp.name)
print(emp.id)
print(emp.skills)
