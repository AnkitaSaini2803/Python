'''Operator Overloading          23/1/2025
You can overload an operator in Python by defining special methods in your class. 
These methods are identified by their names, which start and end with double 
(__). Here are some of the most commonly overloaded operators and their 
corresponding special methods:

+ : __add__
- : __sub__
* : __mul__
/ : __truediv__
< : __lt__
> : __gt__
== : __eq__

'''
class Operator_overloading:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        #  return f"{self.i+x.i}i + {self.j+x.j}j + {self.k+x.k}k"
        return Operator_overloading(self.i+x.i , self.j+x.j , self.k+x.k) #constructor bna diya yhan 
    
op=Operator_overloading(2,6,3)
print(op)

op1=Operator_overloading(7,8,9)
print(op1)

# print(op.add(op1))
print(op+op1)
print(type(op+op1))  #showing string here before

