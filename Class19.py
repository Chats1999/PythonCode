#to print 1/212/32123/4321234/543212345 pyramid

num=5

for i in range(1,num+1):
    for j in range(num-i):
        print(' ', end='')
    for j in range(i,1,-1):
        print(j,end='')
    for j in range(1,i+1):
        print(j,end='')
    print()

#to print box5(nos frpm 1 to 25)
num=5
a=[[0 for i in range(num)]for j in range(num)]
k=1
low=0
high=num-1
for i in range((num+1)//2):
    
    for j in range(low,high+1):
     a[low][j]=k
     k+=1
    for j in range(low+1,high+1):
     a[j][high]=k
     k+=1
    for j in range(high-1,low-1,-1):
     a[high][j]=k
     k+=1
    for j in range(high-1,low,-1):
     a[j][low]=k
     k+=1
    low+=1
    high-=1

    
    



for i in range(num):
    for j in range(num):
        print(a[i][j],end='\t')
    print()    
