
#if the no is repeated add the square of that no or else just add all nos
a=[1,2,5,4]
sum=0
for i in range(len(a)):
    if a.count(a[0])==len(a):
        sum=sum+a[i]**2
        print(sum)
    else:
       sum=sum+a[i]
       print(sum)
#if the no is repeated the no is squared and then added to normal sum 
a=[1,2,4,4]
sum=0
for i in range(len(a)):
    if a.count(a[i])>1:
        sum=sum+a[i]**2
        print(sum)
    else:
        sum=sum+a[i]
        print(sum)


# sqaure the second time the no is repeated

a=[1,2,1,4,4]
b=[]
sum=0
for i in a:
    if i not in b:
        b.append(i)
        sum=sum+i
        print(sum)
    else:
        sum=(sum+i**2)
        print(sum)



        
       
        
        
         
     
         



        
        
               
