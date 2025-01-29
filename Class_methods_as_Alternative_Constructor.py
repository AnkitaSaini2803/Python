''' 20/1/2025
This is a parameterized constructor by default
The most common use-case of class Method as alternative constructor is :
when you want to create an object of class(here Person) from a data like 
string or dictionary which contains data like person's name and its age separated
by (-) or comma or anything else

'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
     
    @classmethod 
    def from_str(cls,string):
        return cls(string.split(',')[0],int(string.split(',')[1]))
    
    
p1=person('RadheFarm', 6)
print(p1.name)
print(p1.age)

string="Ramashyam , 30"
l=person.from_str(string)
print(l.name)
print(l.age)


''''''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

person = Person.from_string("John Doe, 30")
print(person.name, person.age)