#sorting in ascending 
'''
a=[56,0,0,2,2]
for i in range(len(a)-1):
  minv=min(a[i:])
  ind=a.index(minv,i)
  print(minv)
  a[i],a[ind]=a[ind],a[i]
  print(a)
'''
#to print x no of 0's in list
'''x=int(input('input'))
a=[]
for i in range(x):
 a.append(0)
print(a)'''
#to print nos divisible by 3 or 5
'''
x=int(input('enter'))
a=[i for i in range(x) if i%3==0 or i%5==0]
print(a)
'''

#to print the natural nos according to input range
'''
x=int(input('enter a no'))
a=[i+1 for i in range( x)]
print(a)
'''
#List Comprehension
'''
a=[int(i) for i in input('enter').split()]
print(a)
'''
#to add using pointers
'''def add(*a):
    sum1=0

    for i in a:
         sum1=sum1+i
    print(sum1)

add(10,20,30)'''
#to convert string to integer from list
a=input('enter').split()
for i in range(len(a)):
    a[i]=int(a[i])
    print(a)
