#to print EDBCA/EDBC/EDB/ED/E
'''
num=5
for i in range(num,0,-1):
    for j in range(i):
        print(chr(69-j),end=' ')
        
    print("")    
'''
#to print EDBCA/DBCA/CBA/BA/A
'''
num=5
k=69
for i in range(num,0,-1):
    for j in range(i):
        print(chr(k-j),end='')
    k-=1
    
    print(" ")
    '''
#
'''
list1= [5,4,3,2,1]
list2= list1
list1=list1+[1,2,3,4]
print(list1)
print(list2)

list1= [5,4,3,2,1]
list2= list1
list1+=[1,2,3,4]
print(list1)
print(list2)
'''
#to print ----/---/--/-
'''
num=5
for i in range(num,0,-1):
    for j in range(1,i):
        print(' -', end='')
    print()
    '''
#to print ----*/---**/--***/-****/*****
'''
num=5
for i in range(1,num+1):
    
    for j in range(num-i):
        
     print(' ', end='')
    print('*' * i,end=' ')
      
    print()    


num=5
for i in range(1,num+1):
    for j in range(num-i):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
'''
#to print */***/*****/******* pyramid
'''
num=5
for i in range(1,num+1):
    for j in range(num-i):
        print(' ',end='')
    for j in range(i*2-1):
        print('*',end='')
    print()
    '''
#to print *********/*******/*****/***/* inverse pyramid
'''
num=5
k=num
for i in range(1,num+1):
    for j in range(1,i):
      print('- ',end='')
      
    for j in range(k*2-1):
        print(' *',end='')
    k-=1
        
    print()    
'''
