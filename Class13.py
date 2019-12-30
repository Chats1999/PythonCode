#to check the no. is power of 2 or not 
'''
n=int(input('enter a no'))
count=0
while n>1:
    valid=False
    if n%2==0:
        count=count+1
        n=n/2
        valid=True
    else:
     valid=False
     break
   

if valid:
    print('it is a power')
    print(count)
else:
    print('not a power')
'''
#to check it is secret code or not with 3 chances
'''secretno=5
n=int(input('enter a no'))
if n==secretno:
    print('you Won')
else: 
    print('second chance')
    n2=int(input('enter a no'))
    if n2==secretno:
        print('you won')
    else:
     print('third chance')
     n3=int(input('enter a no'))
     if n3==secretno:
         print('you won')
     else:
         print('not the secretcode')
'''
#to check it is secret code or not with 3 chances
'''
secretno=5
count=0
while count<3:
    
  n=int(input('enter a no'))   
  if n==secretno:
    print('you won')
    break
  else:
    print('try again')
    count=count+1
else:
    print('game over') 
'''





