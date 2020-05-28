#This class is base class of all classes here.
class animals() :
    def __init__(self) :
        self.__furcolor = "white"
        self.__numlegs = 4
        self.__numeyes = 2
    def get_furcolor(self) :
        return self.__furcolor
    def get_numeyes(self) :
        return self.__numeyes
    def get_numlegs(self) :
        return self.__numlegs
    def set_furcolor(self,a) :
        self.__furcolor = a
    def set_numlegs(self,b) :
        self.__numlegs = b

#This class inherits animal class and describes habitat of animal as aquatic habitat.
class aquatic(animals) :
    def __init__(self) :
        animals.__init__(self)
    def swim(self) :
        print("Flap your fins and move ahead \n")
    def set_numlegs(self,b) :
        animals.set_numlegs(self,b)
    def set_furcolor(self,a) :
        animals.set_furcolor(self,a)

#This class inherits animal class and describes habitat of animal as air and sky habitat.
class ariel(animals) :
    def __init__(self) :
        animals.__init__(self)
    def fly(self) :
        print("Flap your wings and rise high\n")
    def set_numlegs(self,b) :
        animals.set_numlegs(self,b)
    def set_furcolor(self,a) :
        animals.set_furcolor(self,a)

#This class inherits animal class and describes habitat of animal as land habitat.
class terristrial(animals) :
    def __init__(self) :
        animals.__init__(self)
    def walk(self) :
        print("move ahead using your legs\n")
    def set_numlegs(self,b) :
        animals.set_numlegs(self,b)
    def set_furcolor(self,a) :
        animals.set_furcolor(self,a)

#This class inherits animal class and describes habitat of animal as tree habitat.
class arboreal(animals) :
    def __init__(self) :
        animals.__init__(self)
    def climb(self) :
        print("Grip the tree trunk and push above\n")
    def set_numlegs(self,b) :
        animals.set_numlegs(self,b)
    def set_furcolor(self,a) :
        animals.set_furcolor(self,a)

#All animals below inherit the habitat classes according to their living habitat.

class cat(terristrial) :
    def __init__(self) :
        terristrial.__init__(self)
    def food(self) :
        print("Eats rats,rodents,squirrels and decaying flesh\n")
    def motion(self) :
        terristrial.walk(self)
    def set_numlegs(self,b) :
        terristrial.set_numlegs(self,b)
    def set_furcolor(self,a) :
        terristrial.set_furcolor(self,a)

class monkey(arboreal) :
    def __init__(self) :
        arboreal.__init__(self)
    def food(self) :
        print("Eats fruits,grains and some vegetables\n")
    def motion(self) :
        arboreal.climb(self)
    def set_numlegs(self,b) :
        arboreal.set_numlegs(self,b)
    def set_furcolor(self,a) :
        arboreal.set_furcolor(self,a)

class whale(aquatic) :
    def __init__(self) :
        aquatic.__init__(self)
    def food(self) :
        print("Eats small to moderate fish and aquatic vegetation\n")
    def motion(self) :
        aquatic.swim(self)
    def set_numlegs(self,b) :
        aquatic.set_numlegs(self,b)
    def set_furcolor(self,a) :
        aquatic.set_furcolor(self,a)

class parrot(ariel) :
    def __init__(self) :
        ariel.__init__(self)
    def food(self) :
        print("Eats fruits,grains,berries etc\n")
    def motion(self) :
        ariel.fly(self)
    def set_numlegs(self,b) :
        ariel.set_numlegs(self,b)
    def set_furcolor(self,a) :
        ariel.set_furcolor(self,a)

class hippo(terristrial) :
    def __init__(self) :
        terristrial.__init__(self)
    def food(self) :
        print("fish and decaying flesh\n")
    def motion(self) :
        terristrial.walk(self)
    def set_numlegs(self,b) :
        terristrial.set_numlegs(self,b)
    def set_furcolor(self,a) :
        terristrial.set_furcolor(self,a)

#These are arbitary methods called here to test the working of classes.
#Any other methods of above classes can also be called and tested.

h = hippo()
print("Hippo's motion:")
h.motion()
c = cat()
c.set_furcolor("Brown")
print("Cat's furcolor:")
print(c.get_furcolor())
m = monkey()
print("Monkey's furcolor:")
print(m.get_furcolor())
p = parrot()
print("Parrot's legs:")
p.set_numlegs(2)
print(p.get_numlegs())
w = whale()
print("Whale's motion:")
w.motion()
print("Whale's food:")
w.food()
