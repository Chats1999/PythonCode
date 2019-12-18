#minvalue and maxvalue
'''
a=[2,8,9,3,3,1,6]
maxval=minval=a[0]
for i in a:

    
    if maxval< i:
        maxval=i
    elif minval>i:
        minval=i
    
print(maxval)   
print(minval)
'''
#delete duplication
'''
a=[2,8,9,3,3,3,1,6]
b=[]
for i in a:
     if i  not in b:
          b.append(i)
          

print(b)
,,,

#(1+2+3+4+5)^2-(1^2+ 2^ 2+....5^2)
a=int(input('enter the value'))
sum1=0
sum2=0
for i in range(1,a+1):
     sum1=sum1+(i*i)
     sum2=sum2+i
print(abs(sum1-(sum2)**2))
,,,



      
      


          
