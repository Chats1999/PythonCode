#how much downpayment to pay according to salary
'''
n=int(input('the cost of the good'))
salary=int(input('enter salary'))
if salary>0.4*n:
    print('the downpayment you have to pay',0.1*n)
else:
    print('the downpayment you have to pay is',0.5*n)
'''
#to check if no. is armstrong
'''
a=input('enter a string')
sum1=0
for i in range(len(a)):
 sum1=sum1+(int(a[i])**len(a))
 print(int(a[i]))
 
if sum1==int(a):
 print('it is armstrong')
else:
 print('not armstrong')
 '''
#to print second maximum value using if and elif
'''
a=[1,2,8,2,7,10,29]
maxvalue=a[0]
maxvalue2=0
for i in a:
    if maxvalue<i:
        maxvalue2=maxvalue
        maxvalue=i
    elif maxvalue2<i:
        maxvalue2=i
print(maxvalue2)
'''
#to print second maximum no. using if
'''
a=[1,2,8,2,7,10,29]
maxvalue=a[0]
maxvalue2=0
for i in a:
    if maxvalue<i:
        maxvalue2=maxvalue
        maxvalue=i
    if maxvalue2<i<maxvalue:
        maxvalue2=i
print(maxvalue2)
'''
#to separate the username
'''
a=input('enter your email id')
for i in a:
    if i=='@':
        break
    else:
      print(i,end='')

'''      

#to separate the host
'''

a=input('enter the email')
for i in a[(a.index('@')+1):(a.index('.'))]:
   print(i,end='')
  
 '''
# to check for leap year
'''
year=int(input('enter the year'))
valid=False
if year%4==0:
    valid=True
    if year%100==0:
        valid=False
        if year%400==0:
          valid=True

if valid==True:
    print('it is aleap year')
else:
    print('not a leap year')
'''     



