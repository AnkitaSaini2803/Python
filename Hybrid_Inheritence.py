'''18/1/2025
HYBRID INHERITENCE :- Inheritence consisting of multiple types of ineritence
Here,it consist of Simple_Inheritence + Multiple_Inheritence
'''
class School:
    def school(self):
        print("You are inside school class")
class student1:
    def func1(self):
        print("You are inside student1 class")
class student2(student1):
    def func2(self):
        print("You are inside student2 class ")      
        
class student3(student1,School):
    def func3(self):
        print("You are inside student 3 class")

obj=student3()
obj.school()
obj.func1()
obj.func3()

object=student2()
object.func2()
object.func1()