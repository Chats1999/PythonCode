#forloop

'''

a=[10,20,30,40,50]
b=10
for i in range(0,b):
    print(i,end='')
print('\n')
for i in range(b-1,-1,-1):
    print(i,end='')
'''
'''
a=[10,20,30,40,50]
for i in a:
    print(i,end='')
print('')
for i in range(5):
    print(a[i])
    
'''
#nestedforloop
'''
for i in range(5):
    for j in range(5):
       print(i,j,end='|',sep='-')
'''
'''
a=[2,3,2,9,3,3,1,6]
count=0
for i in a:
    count=count+1
print(count)
'''
'''
a=[2,3,2,9,3,3,1,6]
sum=0
for i in range(len(a)):
    sum= sum+ a[i]
print (sum)
'''

'''
a=[2,3,2,9,3,3,1,6]
num=int(input('enter a no'))
count=0
for i in a:
    if i==num:
        count=count+1
    print(count)    

a=[2,'string',9,3,3,1,6]
s=0 
for i in range(len(a)):
    if type(a[i])==int:
        s=s+a[i]

print(s)
'
'''

a=[2,8,9,3,3,1,6]
for i in range(a):
    if a[i]<a[i+1]:
print a[i+1]
    else:
print a[i]





    
    
