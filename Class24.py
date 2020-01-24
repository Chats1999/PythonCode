'''
class Calc():
    def add(a,b):
        c=a+b
        print (c)
    def sub(a,b):
        c=a-b
        print(c)
Calc.add(10,20)
Calc.sub(30,20)
print('hi')
'''
'''
class Calc():
    def add(self,a,b):
        return (a+b)
    def sub(self,a,b):
        return(a-b)
obj=Calc()
print(obj.add(10,20))
print(obj.sub(50,20))
'''
'''
class Calc():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return (self.a+self.b)
    def sub(self):
        return (self.a-self.b)
obj=Calc(10,20)
print(obj.add())
print(obj.sub())
'''


class StbDb():
    def __init__(self, marks, name):
        self.marks = marks
        self.name = name

    def displayname(self):
        return (self.name)

    def displaymarks(self):
        return (self.marks)

'''
obj = StbDb([50, 70, 80, 90, 100], 'Chaithu')

print(obj.marks)
print(obj.name)
print(obj.displayname())
print(bj.displaymarks())
'''

class Grade(StbDb):

    @property
    def averag(self):
        avg = sum(self.marks) // len(self.marks)
        for i in self.marks:
            if i<50:
                c='grade F'
                break
        else:

            if 50<=avg<=60:
             c = 'Grade D'
            elif 61 <= avg <= 70:
             c = 'Grade E'
            elif 71 <= avg <= 80:
             c = 'Grade C'
            elif 81 <= avg <= 90:
             c = 'Grade B'
            else:
             c = 'Grade A'

        return self.name,avg,c


obj1 = Grade([90,80,70,60,90,99],'Chaithu')
print(obj1.averag)
