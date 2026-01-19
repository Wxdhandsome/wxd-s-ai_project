import math
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return math.pi*self.r**2
    def circumference(self):
        return 2*math.pi*self.r

circle_1=Circle(5)
print(circle_1.area())
print(circle_1.circumference())



class Shape:
    def __init__(self):
        self.area=0
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def area(self):
        return self.w*self.h

rectangle=Rectangle(5,10)
print(rectangle.area())



