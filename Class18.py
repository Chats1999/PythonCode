#to print*/**/***/****/*****/****/***/**/* half diamond

num=6

for i in range(1,num+1):
     for j in range(i,num):
        print(' ',end='')
     for j in range(i,0,-1):
        print('*',end='')
     print()
for i in range(1,num):        
     for j in range(i,0,-1):
        print(' ',end='')
     for j in range(i,num):
        print('*',end='')
     print()   

# TO PRINT*/**/***/****/*****/****/***/**/* diamond

num=3
for i in range(1,num+1):
    for j in range(num-i):
        print(' ',end='')
    for j in range(i):
        print('* ',end='')
    print()
for i in range(1,num+1):
    for j in range(1,i):
        print(' ', end='')
    for j in range(num-i):
        print(' *', end='')
    print()


#to print */***/*****/***/* diamond
num=3
k=0
for i in range(1,num+1):
    for j in range(num-i+1):
        print(' ', end='')
    for j in range(i*2-1):
        print('*', end='')
    print()
for i in range(num,-1,-1):
    for j in range(num-i):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        print(' ', end='')
    for j in range(i*2+1):
        print('*', end='')
       
    print()    



#to use try,except and finally
    
a=[8,9,6,8,7,8,9]
b=3
for i in a:
    try:
        print(i/b)
        b=-1
    except ZeroDivisionError:
        raise
        print('b is zero')
        b=-1
    finally:
            print('finally')



#to use raise exception

kumarmark=[30,45,85,-85,56]
for i in kumarmark:
    if i<0:
        raise Exception["sorry, no numbers below zero"]
    else:
     print(i)

