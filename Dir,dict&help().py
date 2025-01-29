'''20/1/2025'''
a=[5,6,2,3,4]
print(dir(a))

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=person('Ankita',19)
print("\n")
print(dir(person))
print("\n")
print(p.__dict__)
print("\n")
print(help(str))
print("\n")
print(help(person))