''' 18/1/2025
All the variables and methods(member_functions) are Pblic by default'''
class Person:
    def __init__(self,name):
        self.name=name
person1=Person('Ankita Saini')
print(person1.name)

'''Private with (__) double underscore
Without double underscore(__) it prints abhi and 19 but with underscore it is 
throwing error because name and age are now private variables and they cannot be 
accessed from outside the class

'''
class student:
    def __init__(self,name,age):
        self.__name=name      # indication of private variable
        self.__age=age         # indication of private variable
stud=student('Abhi',19)
print(stud.name)
print(stud.age)

'''
Name Mangling is a technique in python used to protect class-private and superclass
-private members and methods to be accidently ovewritten from sub-classes
Provides a way to make an attribute "private" by using double underscore(__)

but they can be accessed by using attribute's name with _ClassName
'''
class Name_Mangling():
    def __init__(self):
        self.__Employee_name='Ankita Saini'
        self._age=19
        self.__occupation='AI Engineer'
object=Name_Mangling()
print(object._age)
print(object._Name_Mangling__Employee_name)
print(object._Name_Mangling__occupation)
# print(object.__Employee_name) #AttributeError: 'Name_Mangling' object has no attribute '__Employee_name'
# print(object.__occupation) #also shows an error
