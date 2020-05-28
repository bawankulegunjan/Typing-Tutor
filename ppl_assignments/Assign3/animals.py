#This program has 10 animal classes followed by calling of their
#respective methods to test these classes.

class cat() :
    def __init__(self,a="black") :
        self.__eyecolor = a
        self.__legs = 4
        self.__furcolor = "yellow"
    def get_legs(self) :
        return self.__legs
    def set_legs(self,a=3) :
        self.__legs = a
    def get_eyecolor(self) :
        return self.__eyecolor
    def set_furcolor(self,b) :
        self.__furcolor = b
    def get_furcolor(self) :
        return self.__furcolor
    def speak(self) :
        print("meow")
    def walk(self) :
        print("jump or crawl")

c1 = cat()
c1.__furcolor()
print("Number of legs of cat are ",c1.get_legs())
c1.set_furcolor("brown")
print("Fur color of cat is ",c1.get_furcolor())

class dog() :
     def __init__(self,a="Brown") :
         self.__eyecolor = a
         self.__legs = 4
     def get_legs(self) :
         return self.__legs
     def set_legs(self,a=4): 
         self.__legs = a
     def get_eyecolor(self) :
         return self.__eyecolor
     def set_eyecolor(self,c) :
         self.__eyecolor = c 
     def set_furcolor(self,b) :
         self.__furcolor = b
     def get_furcolor(self) :
         return self.__furcolor
     def speak(self) :
         print("Dog barks")
     def walk(self) :
         print("Dog jump or brisk-walk or run")
d1=dog()
d1.speak()
d1.walk()
d1.set_eyecolor("Blue")
print("Eyecolor of dog is ",d1.get_eyecolor())
      
class fish() :
    def __init__(self,a="gray",b="black") :
        self.__scalecolor = a
        self.__eyes = 2
        self.__eyecolor = b
        self.__scaletype = "sharp"
    def get_eyes(self) :
        return self.__eyes
    def set_eyes(self,c) :
        self.__eyes = c
    def get_eyecolor(self) :
        return self.__eyecolor
    def get_scalecolor(self) :
        return self.__scalecolor
    def get_scaletype(self) :
        return self.__scaletype
    def swim(self) :
        print("Fishes breathe and mov ahead using gills and fins")
    def eat(self) :
        print("anything from algae to other fish is acceptable")

f = fish()
f.swim()
print("Eye color of fish is ",f.get_eyecolor())
print("Scaletype of fish is ",f.get_scaletype())

class parrot() :
    def __init__(self,a=1,b="green",d=4) :
        self.__eyes = 2
        self.__wingspan = a
        self.__feathercolor = b
        self.__claws = d
    def get_eyes(self) :
        return self.__eyes
    def get_wingspan(self) :
        return self.__wingspan
    def get_feathercolor(self) :
        return self.__feathercolor
    def get_claws(self) :
        return self.__claws
    def set_claws(self,c) :
        self.__claws = c
    def fly(self) :
        print("Flap your wings and rise above")
    def eat(self) :
        print("Eat small insects and fruits")

p = parrot(2,"light green")
p.set_claws(3)
print("Claws for parrot are ",p.get_claws())
p.fly()
p.eat()
print("Feather color for parrot is ",p.get_feathercolor())

class snake() :
    def __init__(self,a=2,b="brown") :
        self.__eyes = a
        self.__scalecolor = b
        self.__pupilshape = "round"
        self.__snaketype = "non venomous"
    def get_eyes(self) :
        return self.__eyes
    def get_scalecolor(self) :
        return self.__scalecolor
    def set_pupilshape(self,c) :
        self.__pupilshape = c
    def get_pupilshape(self) :
        return self.__pupilshape
    def set_snaketype(self,d) :
        self.__snaketype = d
    def get_snaketype(self) :
        return self.__snaketype
    def hiss(self) :
        print("Take tongue out and smell")
    def bite(self) :
        print("Snake Pierce fangs onto something")

s = snake(2,"green")
s.set_pupilshape("elliptical")
print("Pupil shape of snake is ",s.get_pupilshape())
s.bite()
s.set_snaketype("venomous")
print("Snake is ",s.get_snaketype())

class crocodile() :
    def __init__(self,a=4,b="yellow ochre") :
        self.__legs = a
        self.__scalecolor = b
        self.__bitepower = "1000 psi"
        self.__type = "Indian crocodile"
    def get_legs(self) :
        return self.__legs
    def get_scalecolor(self) :
        return self.__scalecolor
    def set_bitepower(self,c) :
        self.__bitepower = c
    def get_bitepower(self) :
        return self.__bitepower
    def set_type(self,d) :
        self.__type = d
    def get_type(self) :
        return self.__type
    def swim(self) :
        print("Crocodile Float and move with the help of tail")
    def eat(self) :
        print("Mainly fish")
    def walk(self) :
        print("Move ahead with 4 legs")

c2 = crocodile(4,"light brown")
c2.swim()
#c2.__type()
print("Bite power of crocodile is ",c2.get_bitepower())

class giraffe() :
    def __init__(self,a=4,b="brown checks") :
        self.__legs = a
        self.__pattern = b
        self.__height = "10 feet"
    def get_legs(self) :
        return self.__legs
    def get_pattern(self) :
        return self.__pattern
    def set_height(self,c) :
        self.__height = c
    def get_height(self) :
        return self.__height
    def eat(self) :
        print("Mainly tree leaves")
    def walk(self) :
        print("Move ahead with long steps")

g = giraffe(4,"light yellow")
g.walk()
g.set_height("11 feet")
print("Height of giraffe is ",g.get_height())

class tiger() :
    def __init__(self,a="black") :
        self.__eyecolor = a
        self.__legs = 4
        self.__furcolor = "yellow"
        self.__furpattern = "black stripes"
    def get_legs(self) :
        return self.__legs
    def set_legs(self,a=4) :
        self.__legs = a
    def get_eyecolor(self) :
        return self.__eyecolor
    def set_furcolor(self,b) :
        self.__furcolor = b
    def get_furcolor(self) :
        return self.__furcolor
    def get_furpattern(self) :
        return self.__furpattern
    def set_furpattern(self,c) :
        self.__furpattern = c
    def speak(self) :
        print("roar")
    def walk(self) :
        print("jump or crawl or leap")

t = tiger()
t.set_furcolor("brown")
print("Fur color of tiger is ",t.get_furcolor())
print("Fur pattern of tiger is ",t.get_furpattern())

class monkey() :
    def __init__(self,a="brown") :
        self.__legstowalk = 4
        self.__furcolor = a
        self.__type = "langur"
        self.__habitat = "tall trees"
    def get_furcolor(self) :
        return self.__furcolor
    def get_legstowalk(self) :
        return self.__legstowalk
    def set_legstowalk(self,b) :
        self.__legstowalk = b
    def get_type(self) :
        return self.__type
    def set_type(self,c) :
        self.__type = c
    def get_habitat(self) :
        return self.__habitat
    def set_habitat(self,d) :
        self.__habitat = d
    def climb(self) :
        print("Monkey Hold tree trunk and move above")
    def walk(self) :
        print("Move on ground using 4 or 2 legs")
    def eat(self) :
        print("Mainly fruits")

m = monkey("reddish brown")
m.climb()
m.set_habitat("branches")
print("Habitat of monkeys is ",m.get_habitat())

class lizard() :
    def __init__(self,a=4,b="pointed") :
        self.__claws = a
        self.__scales = b
        self.__size = "1 feet"
    def get_claws(self) :
        return self.__claws
    def get_scales(self) :
        return self.__scales
    def get_size(self) :
        return self.__size
    def set_size(self,c) :
        self.__size = c
    def grab(self) :
        print("Hold something tightly with claws")
    def eat(self) :
        print("Lizards eat Small insects and worms")

l = lizard(4,"spiny")
l.eat()
print("Scales of lizard are ",l.get_scales())

