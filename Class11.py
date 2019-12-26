#to print the maximum palindrome numbers that can be made as a product of two two digit nos
'''
n=int (input('enter the lowerlimit'))
t=int(input('enter  the upperlimit'))
maxval=0
for i in range(n,t):
 for j in range(n,t):
     a=(i*j)
     b=str(a)
     if str(a)==b[: :-1]:
         if maxval<a:
            maxval=a
            x,y=i,j

print(maxval,x,y)
         
'''

#to replace bita by bktc
'''       
   
word=input('enter a string')
for i in word:
    if i =='i'or i=='e' or i=='a'or i=='o'or i=='u':
        word =word.replace(i,(chr(ord(i)+2)))
print(word)
'''

#to replace bita by bktc        

'''
word=input('enter a string')
list=['a','e','i','o','u']
for i in word:
    if i in list:
        word=word.replace(i,(chr(ord(i)+2)))
        
print(word)         
    
'''
#to replace bita by bktc
'''
word=input('enter a string')
list=['a','e','i','o','u']
for i in word:
    if  i in list:
        print(chr(ord(i)+2),end='')
    else:
        print(i,end='')
'''
#to check 2^n==the given no.
'''
num=int(input('enter a no'))
for n in range(1,99):
    if 2**n==num:
     print('yes')
     break
     
else:
    print('no')
'''
#to check brackets valid or not
a=input('enter a string')
openb= ['(','[','{']
close=[')',']','}']
count=0
for i in range(len(a)//2):
    
    count=count-1
    
    if close[openb.index(a[i])]!=a[count]:
             print('invalid')
             break
else:
    print('Valid')
        
            
                

