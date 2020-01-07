# to print number series from 1 /23 /456/ 78910
'''
rows=5

num=1
for i in range(rows):
    for j in range(i +1):
        print(num,end=' ')
        num+=1
    print("")

'''
#to sort numbers using bubble sorting
'''
def sort(a):
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a


a=[1,9,4,6,1,5]
print(sort(a))
'''
# to print 12345/1234/
'''
num=5
for i in range(num,0,-1):
    for j in range(i):
        print(j+1, end='')
        
    print("")

'''
#to print 1/123/12345 and so on
'''
num=5
k=1
for i in range(num):
    for j in range(0,k):
        print(j+1,end=' ')
    k+=2        
    print("")    

'''
#to print 1/123/12345 and so on
'''
num=5
for i in range(1,num+1):
    i=i*2-1
    for j in range(1,i+1):
        print(j,end=' ')
    print()

'''
#to print A/AB/ABC and so on
num=5
for i in range(1,num):
      
    for j in range(i):
        print(chr(65+j), end='')

    print(" ")    
       

    





