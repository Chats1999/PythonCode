def addition(a=10,b=50):
        c=a+b
        print(c)
def subraction(a,b):
        c=a-b
        print(c)
                       

def palindrome(string):
        if string==string[::-1]:
                print('palindrome')
        else:
                 print('not a palindrome')

def greeting(name,course,inst='bita'):
        print('hi{}Welcome to{}your Course is{}'.format(name,inst,course))
if __name__=='__main__':
        palindrome('malayalam')
        addition()
        subraction()
        greeting('raj','python')
        greeting('kumar','python','tata')
                       
