'''
class Dog():
    def sound(self):
        print('bark')
class Cat():
    def sound(self):
            print('meow')
def mammal(animal):
print(animal.sound())
dogobj=Dog()
catobj=Cat()
mammal(catobj)
'''
'''

class BaseClass():
    print('hai')
    def __init__(self,water):
        print('base')
        self.test_water=water
        '''


class OLdcalc():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sub(self):
        print(self.b - self.a)


class NewCalc(Oldcalc):
    def sub(self):
        print(self.b - self.a)
        super(NewCalc, self).sub()


obj = NewCalc(20, 10)
obj.sub()
