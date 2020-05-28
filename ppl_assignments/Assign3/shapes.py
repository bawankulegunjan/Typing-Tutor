#This program contains 10 classes of shapes followed by calling of their 
#respective methods to test these classes.

import turtle
import math

class circle() :
    def __init__(self,a=10) :
        self.__r = a
    def set__radius(self,b) :
        self.__r = b
    def get_radius(self) :
        return self.__r
    def get_area(self) :
        return (3.142*self.__r*self.__r)
    def get_perimeter(self) :
        return (2*3.142*self.__r)
    def draw(self) :
        turtle.circle(self.__r)

c = circle(100)
c.draw()
#c.__r()
print("Area of circle is ",c.get_area())

class square() :
    def __init__(self,a=10) :
        self.__s = a
    def get_side(self) :
        return self.__s
    def set_side(self,b) :
        self.__s = b
    def get_area(self) :
        return (self.__s*self.__s)
    def get_perimeter(self) :
        return (4*self.__s)
    def draw(self) :
        turtle.goto(self.__s,0)
        turtle.goto(self.__s,self.__s)
        turtle.goto(0,self.__s)
        turtle.goto(0,0)

s = square(100)
s.draw()

class rectangle() :
    def __init__(self) :
        self.__length = 10
        self.__breadth = 5
    def get_length(self) :
        return self.__length
    def get_breadth(self) :
        return self.__breadth
    def set_length(self,a) :
        self.__length = a
    def set_breadth(self,b) :
        self.__breadth = b
    def perimeter(self) :
        return 2*(self.__length + self.__breadth)
    def area(self) :
        return (self.__length * self.__breadth)
    def draw(self) :
        turtle.goto(self.__length,0)
        turtle.goto(self.__length,self.__breadth)
        turtle.goto(0,self.__breadth)
        turtle.goto(0,0)

r = rectangle()
print("Area of rectangle is ",r.area())
r.draw()
r.set_breadth(100)
r.set_length(200)
print("Perimeter of rectangle is ",r.perimeter())
r.draw()

class regpentagon() :
    def __init__(self) :
        self.__side = 100
    def get_side(self) :
        return self.__side
    def set_side(self,a) :
        self.__side = a
    def perimeter(self) :
        return 5*(self.__side)
    def area(self) :
        return (5*self.__side*self.__side)/(4*math.tan(3.142/5))
    def draw(self) :
        turtle.forward(self.__side)
        for i in range(0,4) :
            turtle.right(-72)
            turtle.forward(self.__side)
        turtle.right(-72)

p = regpentagon()
print("Perimeter of pentagon is ",p.perimeter())
p.draw()

class reghexagon() :
    def __init__(self) :
        self.__side = 100
    def get_side(self) :
        return self.__side
    def set_side(self,a) :
        self.__side = a
    def perimeter(self) :
        return 6*(self.__side)
    def area(self) :
        return (6*1.7321*self.__side*self.__side)/4
    def draw(self) :
        turtle.forward(self.__side)
        for i in range(0,5) :
            turtle.right(-60)
            turtle.forward(self.__side)
        turtle.right(-60)

h = reghexagon()
print("Area of hexagon is ",h.area())
h.draw()

class regoctagon() :
    def __init__(self) :
        self.__side = 100
    def get_side(self) :
        return self.__side
    def set_side(self,a) :
        self.__side = a
    def perimeter(self) :
        return 8*(self.__side)
    def area(self) :
        return (2*(1 + 1.414)*self.__side*self.__side)
    def draw(self) :
        turtle.forward(self.__side)
        for i in range(0,7) :
            turtle.right(-45)
            turtle.forward(self.__side)
        turtle.right(-45)

o = regoctagon()
print("Perimeter of octagon is ",o.perimeter())
o.draw()

class regtriangle() :
    def __init__(self) :
        self.__side = 100
    def get_side(self) :
        return self.__side
    def set_side(self,a) :
        self.__side = a
    def perimeter(self) :
        return 3*(self.__side)
    def area(self) :
        return (1.7321*self.__side*self.__side)/4
    def draw(self) :
        turtle.forward(self.__side)
        for i in range(0,2) :
            turtle.right(-120)
            turtle.forward(self.__side)
        turtle.right(-120)

t = regtriangle()
print("Perimeter of equilateral triangle is ",t.perimeter())
t.draw()

class regtrapezium() :
    def __init__(self) :
        self.__eqsides = 50
        self.__lside = 100
    def get_eqsides(self) :
        return self.__eqsides
    def get_side(self) :
        return self.__lside
    def set_eqsides(self,a) :
        self.__eqsides = a
    def set_lside(self,b) :
        self.__lside = b
    def perimeter(self) :
        return (5*self.__eqsides)
    def area(self) :
        return (3*self.__eqsides*self.__eqsides*1.7321)/4
    def draw(self) :
        turtle.forward(self.__lside)
        turtle.right(-120)
        turtle.forward(self.__eqsides)
        turtle.right(-60)
        turtle.forward(self.__eqsides)
        turtle.right(-60)
        turtle.forward(self.__eqsides)
        turtle.right(-120)

t1 = regtrapezium()
print("Perimeter of trapezium is ",t1.perimeter())
t1.draw()

class righttriangle() :
    def __init__(self) :
        self.__s1 = 3
        self.__s2 = 4
        self.__hyp = (self.__s1**2 + self.__s2**2)**(1/2)
    def get_s1(self) :
        return self.__s1
    def get_s2(self) :
        return self.__s2
    def get_hyp(self) :
        return self.__hyp
    def set_s1(self,a) :
        self.__s1 = a
    def set_s2(self,b) :
        self.__s2 = b
    def perimeter(self) :
        return (self.__s1 + self.__s2 + self.__hyp)
    def area(self) :
        return (self.__s1*self.__s2)/2
    def draw(self) :
        turtle.goto(0,self.__s1)
        turtle.goto(self.__s2,0)
        turtle.goto(0,0)

r1 = righttriangle()
r1.draw()
print("Area of right angled triangle is ",r1.area())
r1.set_s1(300)
r1.set_s2(400)
r1.draw()

class regrhombus() :
    def __init__(self) :
        self.__side = 100
    def get_side(self) :
        return self.__side
    def set_side(self,a) :
        self.__side = a
    def perimeter(self) :
        return 4*self.__side
    def area(self) :
        return (2*self.__side*self.__side*1.7321)/4
    def draw(self) :
        turtle.forward(self.__side)
        turtle.right(-60)
        turtle.forward(self.__side)
        turtle.right(-120)
        turtle.forward(self.__side)
        turtle.right(-60)
        turtle.forward(self.__side)
        turtle.right(-120)

r2 = regrhombus()
r2.draw()
r2.set_side(200)
print("Side of rhombus is ",r2.get_side())
print("Perimeter of rhombus is ",r2.perimeter())

