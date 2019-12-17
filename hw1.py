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
a=[2,8,9,3,3,3,1,6]
b=[]
for i in a:
     if i  not in b:
          b.append(i)
          

print(b)          
          
                
     
