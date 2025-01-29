# '''1                                      25/1/2025'''
# class A:
#     def test1(self):
#         print("method named test1 of A called")


# class B(A):
#     def test1(self):
#         print("method named test1 of B called")


# class C(A):
#     def test1(self):
#         print("method named test1 of C called")


# class D(B, C):
#     def test2(self):
#         print("method named test2 of D called")

# object1=D()
# print(D.mro())
# object1.test1()

# #2
# s = "abcd"
# b = s + "ef"
# print(s)

# #3
# z = True and False
# print(z)

# #4
# def fun(n):
#     n=9
#     return n
# n=19
# fun(n)  #n=fun(n)  --> 9
# print(n)   #19

# ''' In the above code snippet the first two values will be store in the a and b 
# rest of them will be store in *args. 3*1=3,3*4=12,12*5=60 sm=60'''
# def findsum(a,b,*args):

#     sm = 1
#     for i in args:
#         sm *= i
#     return sm
 
# #Driver's code
# z = findsum(1,2,3,4,5)
# print(z)



# large_number = 1000000000000
# print(type(large_number))

# num1 =42
# num2 =-123
# num3 =0

# num4 =0b1010 # represents decimal 10
# num5 =-0B110 # represents decimal -6

# num6 =0o52 # represents octal 42
# num7 =-0O76 # represents octal -62

# num8 =0x2A # represents hexadecimal 42
# num9 =-0X1A # represents hexadecimal -26

# print(type(num1),type(num2),type(num3),type(num4),type(num6),type(num8))
# num1 =18.5
# num2 =87.3
# print(type(num1), type(num2))


# a =True
# b =False
# c =a and b
# d =a or b
# print(c,d)

# def square(a):
#     ans = a * a
#     return ans

# #Driver's code
# a = 4
# a = square(a)
# print(a)


# strType = "CodingNinjas"
 
# # printing string converting to tuple
# tupleType = tuple(strType)
# print("After converting string to tuple : ")
# print(tupleType)
# print("Data type of the tupleType :",type(tupleType))
 
# # printing string converting to set
# setType = set(strType)
# print("After converting string to set : ")
# print(setType)
# print("Data type of the setType :",type(setType))
 
# # printing string converting to list
# listType = list(strType)
# print("After converting string to list : ")
# print(listType)
# print("Data type of the listType :",type(listType))


#29/1/2025

x = 3
y = 9

# bitwise and operator
print(x & y)

# bitwise or operator
print(x | y)

# bitwise not operator
print(~ x)

# bitwise xor operator
print(x ^ y)

# bitwise right shift operator
print(x >> y)

# bitwise left shift operator
print(x << y)



def switch_case(case):  
        switcher = {
            1: "Ninja 1",
            2: "Ninja 2",
            3: "Ninja 3"     }
        result = switcher.get(case, "Invalid choice")
        print(result)
switch_case(1)
switch_case(2)
switch_case(3)
switch_case(4)



class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y if y != 0 else "Cannot divide by zero"

    def case_default(self, x, y):
        return "Invalid operation"

    def execute(self, operation, x, y):
        switcher = {
            "add": self.add,
            "subtract": self.subtract,
            "multiply": self.multiply,
            "divide": self.divide
        }
        method = switcher.get(operation, self.case_default)  # Get the method or default
        return method(x, y)  # Call the method

# Example Usage
calc = Calculator()
print(calc.execute("add", 10, 5))       # Output: 15
print(calc.execute("multiply", 3, 4))   # Output: 12
print(calc.execute("unknown", 3, 4))    # Output: "Invalid operation"
