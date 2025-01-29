'''MULTIPLE INHERITENCE             17/1/2025
When derived class inherit from more than one(two or more) base class'''
class A:
    mother=''
    def func1(self,name):
         self.Mother_name=name
class B:
     father=''
     def func2(self,name2):
          self.Father_name=name2
class C(A,B):
     def parents(self):
          print(f"My mother Name is {self.Mother_name} and Father Name is {self.Father_name}")
obj=C()
obj.Mother_name='Parveen Saini' 
obj.Father_name='Randhir Singh'
obj.parents()    

'''HIERARCHICAL INHERITENCE : When more than one derived class is inherited from
a single base class
'''
class Parent:
     def func(self):
          print("This is parent class")
class child1(Parent):
       def func1(self):
          print("You are inside child 1 of parent class")
class child2(Parent):
        def func2(self):
         print("You are child 2 of parent class")

obj1=child1()
obj2=child2()
obj1.func()
obj1.func1()

obj2.func()
obj2.func2()
