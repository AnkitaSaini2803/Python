'''16/1/2025
DEFAULT CONSTRUCTOR which doesn't have any arguments except self'''
# class person():
#     def __init__(self):
#         print("You are a person")
# object=person()
# object1=person()
# object3=person()   

'''Parameterized Constructor'''
class person():
    def __init__(self,name,occup):
        self.name=name
        self.occupation=occup

    def data(self):
      print(f"{self.name} is a {self.occupation}")

person1=person('Ankita','AI ENGINEER')
# person0=person() This shows a type error because we need to
#  give three arguments here includeing self
# person2=person(1,2,4) Also here error will be generated because there is a
# requirement of 3 arguments but you gave 4 (self,1,2,4)
person2=person('Atharv','HR')
person3=person('Abhi','Doctor')
person1.data()
person2.data()
person3.data()
