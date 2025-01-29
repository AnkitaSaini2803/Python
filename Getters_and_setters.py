''' 17/1/2025
Getter is used to return the value of a specific property, and are typically
defined using the @property decorator.

We cannot set the value through getter method.For that we need setter method
that is defined by @property_name.setter

Here is an example of a class with a getter method and setter method:
#
using single underscore(_)as a prefix before the name of variable or method is used
to indicate that they are intended to be private-->but still can be accessed from
outside the class
#
****
In this example, the person class has a single property, _name,
which is initialized in the init method. The name method is defined as
a getter using the @property decorator, and is used to return the value of 
the _name property.

1)
'''
class person:
    def __init__(self,name):
        self._name=name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,newName):
         self._name=newName
    
person1=person('Ankita')
person1.name='Ankita Saini'
print(person1.name)

'''2) Another Example to find sum of two numbers'''
class My_class:
    def __init__(self,num_1,num_2):
        self._num1=num_1
        self._num2=num_2

    @property
    def num_1(self):
        return self._num_1
    
    @property
    def num_2(self):
        return self._num_2
    

    @num_1.setter
    def num_1(self,val_1):
        self._num_1=val_1

    @num_2.setter
    def num_2(self,val_2):
        self._num_2=val_2
    
    @property
    def sum(self):
        return self.num_1+self.num_2

obj=My_class(15,5)

obj.num_1=90
obj.num_2=23

print(obj.num_1)   #update num_1
print(obj.num_2)   #update num_2
print(obj.sum)



    
