'''Overriding in python       21/1/2025'''
class Shapes:
    def area(self,radius):
        pass
class Circle(Shapes):
    def area(self,radius):
        self.radus=radius
        return 3.14*radius*radius

a1=Circle()
print(a1.area(5))


'''Using SUPER Keyword'''
class Shapes:
    def area(self,radius):
        self.radius=radius
class Circle(Shapes):
        def area(self,radius):
         super().area(radius)
         return 3.14*radius*radius

c2=Circle()
print(c2.area(4))