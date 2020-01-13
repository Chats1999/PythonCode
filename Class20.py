#to print 5 rows and columns with 3 boxes 3, 2,1

num=5
a=[[0 for i in range(num)]for j in range(num)]
k=3
low=0
high=num-1
for i in range((num+1)//2):
    
    for j in range(low,high+1):
     a[low][j]=k
    for j in range(low+1,high+1):
     a[j][high]=k
    for j in range(high-1,low-1,-1):
     a[high][j]=k
    for j in range(high-1,low,-1):
     a[j][low]=k
    low+=1
    high-=1
    k-=1
    
    



for i in range(num):
    for j in range(num):
        print(a[i][j],end='\t')
    print()
    
#to print 5 rows and columns with 3 boxes 3,2,1

num=3
a=[[0 for i in range((num*2)-1)]for j in range((num*2)-1)]
k=3
low=0
high=((num*2)-1)-1
for i in range((num*2)//2):
    
    for j in range(low,high+1):
     a[low][j]=k
    for j in range(low+1,high+1):
     a[j][high]=k
    for j in range(high-1,low-1,-1):
     a[high][j]=k
    for j in range(high-1,low,-1):
     a[j][low]=k
    low+=1
    high-=1
    k-=1
    
    



for i in range((num*2)-1):
    for j in range((num*2)-1):
        print(a[i][j],end='\t')
    print()
    



        

