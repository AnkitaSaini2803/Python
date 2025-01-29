'''Without passing self as an argument in a function ,we created a function 
within a class '''
class Function:
    @staticmethod
    def add(a,b):
        return a+b
    
fun=Function()
print(fun.add(30,50))

