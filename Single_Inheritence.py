''' 17/1/2025
Syntax of INHERITENCE 
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
'''
class Employee:
    def __init__(self,name,emp_id):
        self.Name=name
        self.Employee_Id=emp_id

    
    def display_details(self):
        print(f"The ID of Employee {self.Name} is {self.Employee_Id}")

class Child(Employee):
    def func(self):
        print(f"{self.Name} is attending Python lecture")

emp1=Employee('Aakash',45)
emp1.display_details()
emp2=Child('Ankita',1)
emp2.func()

'''23/1/2025 '''
class Animal:
    def __init__(self):
        print("This is Animal Class")
    
    def animal_sound(self):
        print("Animals Make A Sound")
    
class Cat(Animal):
    def __init__(self,name_of_cat,food):
        print("This is Cat Class")
        self.name=name_of_cat
        self.food=food
        
    def __str__(self):
     return f"The name of cat is {self.name} And She loves to eat {self.food}"
             
    def animal_sound(self):
        print("Cat communicate through Meow")
        

animal=Animal()
animal.animal_sound()
cat1=Cat('Rosy','Burger')
print(str(cat1))
cat1.animal_sound()
