#Multilevel Inheritance

class OldCalc():
    c=100
    def add(a,b):
        c=a+b
        print(c)
    def sub(a,b):
        c=a-b
        print(c)
OldCalc.add(20,30)
print(OldCalc.c)

class NewCalc(OldCalc):
    def mul(a,b):
        return(a*b)
class ModernCalc(NewCalc):
    def pow(a,b):
        print(a**b)

ModernCalc.add(12,30)
print(ModernCalc.mul(23,20))


#multiple Inheritance
        
class OldCalc():
    c=100
    def add(a,b):
        c=a+b
        print(c)
    def sub(a,b):
        c=a-b
        print(c)
OldCalc.add(10,20)
print(OldCalc.c)

class NewCalc():
    def mul(a,b):
        return(a*b)

    
class ModernCalc(NewCalc,OldCalc):
    def pow(a,b):
       print(a**b)


class OldCalc():
    print('bye')
    def __init__(self,a,b):
     self.a=a
     self.b=b

    def add(self):
        c=self.a+self.b
        return c

    def sub(self):
        c=self.a-self.b
        return c

clsoby=OldCalc(20,10)
print(clsoby.add())
print(clsoby.sub())

        
        
