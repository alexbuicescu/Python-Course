__author__ = 'Alexandru'


class Pet(object): #new style class because it inherits 'object'
    """Class that describes a pet"""
    y = 0
    #protected:
    _variabila = 3
    #private:
    __variabila2 = 4
    #Constructorul:
    def __init__(self, name, weight=5):
        self.weight = weight
        self.__name = name

    def __str__(self):
        return 'My pet: ' + str(self.weight) + ' ' + self.__name

    def setx(self, x):
        self.x = x
    def printx(self):
        print self.x

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    name = property(get_name, set_name)


p = Pet('my pet')
p.x = 3
p.setx(3)
print "x = ", p.x
print "y = ", p.y
print str(p)
print p.name
p.printx()


class Cat(Pet):
    """ """
    def __init__(self, name, nr_lives):
        super(Cat, self).__init__(name)
        self.nr_lives = nr_lives


myCat = Cat('nana', 3)
print myCat.weight
print myCat.nr_lives