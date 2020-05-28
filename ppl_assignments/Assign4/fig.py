import math
import turtle

#This is the base class of all classes.
#Virtual functions have no body for function i.e. pass, are abstract classes
class shapes() :
    def perimeter(self) :
        pass
    def area(self) :
        pass
    def draw(self) :
        pass

#The classes below inherit the base class.

class regular(shapes) :
    def __init__(self) :
        self.__numsides = 3
        self.__sidelen = 100
    def get_numsides(self) :
        return self.__numsides
    def set_numsides(self,a) :
        self.__numsides = a
    def get_sidelen(self) :
        return self.__sidelen
    def set_sidelen(self,b) :
        self.__sidelen = b
    def perimeter(self) :
        return (self.__numsides*self.__sidelen)
    def draw(self) :
        turtle.forward(self.__sidelen)
        for i in range(1,self.__numsides) :
            turtle.right(-360/self.__numsides)
            turtle.forward(self.__sidelen)
        turtle.right(-360/self.__numsides)

class nonregular(shapes) :
    def __init__(self) :
        self.__numsides = 3
    def get_numsides(self) :
        return self.__numsides
    def set_numsides(self,a) :
        self.__numsides = a

#The few classes below inherit the regular class.

class regtriangle(regular) :
    def __init__(self) :
        regular.__init__(self)
        regular.set_numsides(self,3)
    def area(self) :
        return (1.7321*self.__sidelen*self__sidelen)/4
    def perimeter(self) :
        return regular.perimeter(self)
    def draw(self) :
        regular.draw(self)

class regsquare(regular) :
    def __init__(self) :
        regular.__init__(self)
        regular.set_numsides(self,4)
    def area(self) :
        return (self.__sidelen*self.__sidelen)
    def perimeter(self) :
        return regular.perimeter(self)
    def draw(self) :
        regular.draw(self)

class reghexagon(regular) :
    def __init__(self) :
        regular.__init__(self)
        regular.set_numsides(self,6)
    def area(self) :
        return (3*1.7321*self.__sidelen*self.__sideleng)
    def perimeter(self) :
        return regular.perimeter(self)
    def draw(self) :
        regular.draw(self)

class regpentagon(regular) :
    def __init__(self) :
        regular.__init__(self)
        regular.set_numsides(self,5)
    def area(self) :
        return (5*self.__sidelen*self.__sidelen)/(4*math.tan(3.142/5))
    def perimeter(self) :
        return regular.perimeter(self)
    def draw(self) :
        regular.draw(self)

class regoctagon(regular) :
    def __init__(self) :
        regular.__init__(self)
        regular.set_numsides(self,8)
    def area(self) :
        return (2*(1 + 1.414)*self.__sidelen*self.__sidelen)
    def perimeter(self) :
        return regular.perimeter(self)
    def draw(self) :
        regular.draw(self)

#The few classes below inherit the nonregular class.

class righttriangle(nonregular) :
    def __init__(self) :
        nonregular.__init__(self)
        self.__s1 = 3
        self.__s2 = 4
        self.__hyp = ((self.__s1**2)*(self.__s2**2))**(0.5)
    def perimeter(self) :
        return (self.__s1 + self.__s2 + self.__hyp)
    def area(self) :
        return (0.5*self.__s1*self.__s2)
    def get_sides(self) :
        return self.__s1,self.__s2,self.__hyp
    def set_sides(self,a,b,c) :
        self.__s1 = a
        self.__s2 = b
        self.__hyp = c

class rectangle(nonregular) :
    def __init__(self) :
        nonregular.__init__(self)
        nonregular.set_numsides(self,4)
        self.__length = 30
        self.__breadth = 40
    def area(self) :
        return (self.__length*self.__breadth)
    def perimeter(self) :
        return 2*(self.__length + self.__breadth)
    def get_sides(self) :
        return self.__length,self.__breadth
    def set_sides(self,a,b) :
        self.__length = a
        self.__breadth = b

#These methods are called to test the above classes.
#Any other methods can also be called to test them.

s = regsquare()
print("no. of sides of square:",s.get_numsides())
print("perimeter of square:",s.perimeter())
s.draw()

o = regoctagon()
print("no. of sides of octagon:",o.get_numsides())
o.draw()

re = rectangle()
print("no. of sides of rectangle:",re.get_numsides())
re.set_sides(20,40)
print("area of rectangle :",re.area())

eq = regtriangle()
print("perimeter of triangle:",eq.perimeter())

t1 = righttriangle()
print("area of right angled triangle :",t1.area())

h = reghexagon()
h.set_sidelen(50)
h.draw()

