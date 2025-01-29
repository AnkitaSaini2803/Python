'''Class Methods                                20/1/2025'''
class Company:
    name='Amazon'
    def func(self):
        # self.name='Tesla'
        self.emp_name='Ankita Saini'
        print(f"The name of company is {self.name}")
        print(f" and AI engineer working here is {self.emp_name}")
    
    # def func(tinde):
    #      tinde.name='TESLA'
    #      tinde.emp_name='Ankita Saini'
    #      print(f"The name of company is {tinde.name}")
    #      print(f" and AI engineer working here is {tinde.emp_name}")

    # @classmethod
    # def func2(tindegobhi,new_name):
    #      tindegobhi.name=new_name
    #      tindegobhi.emp_name='Ankita'
    #      print(f"The name of company is {new_name}")
    #      print(f" and AI engineer working here is {tindegobhi.emp_name}")
    @classmethod
    def func2(cls,new_name):
         cls.name=new_name
         cls.emp_name='Ankita'
         print(f"The name of company is {new_name}")
         print(f" and AI engineer working here is {cls.emp_name}")
    
comp=Company()
comp.func()
comp=Company()
comp.func2('Apple')
print(Company.name)
print(Company.emp_name)
Company.func2('GOOGLE') #Called on a class (e.g., ClassName.func2()) or an instance.
print(Company.name)