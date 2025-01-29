''' 21/1/2025
Dunder/Magic methods are special methods that you can define inside a class
Most commonly used Dunder methods are 
__init__ method  
__len__ method
__call__ method
__str__ method
__repr__ method
'''

class Employee:
    def __init__(self,name):
        self.name=name
   
    def __len__(self):
        i=0
        for j in self.name:
            i=i+1
        return i
    
    def __str__(self):
         return f"The name of HEAD of employee is {self.name},str"
    
    def __repr__(self):
        return f"The name of HEAD of employee is {self.name} ,repr"
    
    
    def __call__(self):
        print(f"I am good") 
    
