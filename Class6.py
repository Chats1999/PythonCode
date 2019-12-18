#to find if divisible by 3 or 5, 3 and 5
'''
a=int(input('enter the starting of th range'))
n=int(input('enter the end of range'))      
for i in range(a,n):
    if i%3==0 | i%5==0
     print(i,'is divisible by 3 or 5')
    if i%5==0& i%3==0:
     print(i,'divisible by both')
'''

#to check elements in a are there in b
'''

   a=[10,20,30]
b=[10,20,30]
for i in range(0,len(a)):
    if a[i]==b[i]:
        print('yes')
    else:
        print('no')
'''

#factorial

'''
n=(int(input('enter a no')))
fact=1
for i in range(n,0,-1):
    print(i)
    fact=fact*i
print(fact)
'''
# Fibonacci series
'''
n=int(input('enter a no'))
a=int(input('enter a no'))
b=int(input('enter a no'))
for i in range(0,n):
    c=a+b
    a=b
    b=c
    print(c)

'''
# to find prime no.
'''
    n=int(input('enter a no'))
for i in range(2,n):
    if n%i==0:
        if n!=i:
         print('not prime')
         break
    else:
          print('prime')
         break

'''
# to print no,alphabets and special Characters seperatly

a='abc$123$#92fg'
for i in a:
    if i.isalpha():
        print(i,end='')
print()        
for i in a:
    if i.isdigit():
      print(i,end='')
print()    
for i in a:    
    if not i.isalnum():
      print(i,end='')
print()    
    
