'''MULTI-LEVEL INHERIITENCE                           17/1/2025
when derived class inherits from another derived class
'''
class Grandfather:
    def __init__(self,g_name):
        self.g_name=g_name

class Father(Grandfather):
    def __init__(self,f_name,g_name):
        self.f_name=f_name
        Grandfather.__init__(self,g_name) #this will call the Grandfather class __
# init__ method from within the father class __init__method

class Son(Father):
    def __init__(self,son_name,f_name,g_name):
        self.son_name=son_name
        Father.__init__(self,f_name,g_name)#this will call the father class __
# init__ method from within the son class __init__method
        
    def details(self):
     print(f"The Grandfather Name is {self.g_name}")
     print(f"The Father Name is {self.f_name}")
     print(f"The Son Name is {self.son_name}")
son1=Son('Rampal Singh','SomNath','Vasudev')
son1.details()

