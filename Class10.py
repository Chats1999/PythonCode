
#to print numbers between the given interval
'''
a=int(input('enter a no'))
b=int(input('enter a no'))

for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
            
    '''

#to display name, gmail and birthdate from list
'''
inputdate=input('enter a date')
a=['10Dec','15 may','15 may']
b=['Chats','Tejasvini','raj']
c=['chatsajit@gmail.com','tej@gmail.com','raj@gmail.com']
for i in range(len(a)):
            if a[i]==inputdate:
                
                 print(' To {} todays date {} Hi {} bitaacademy wishes your a great happy birthday'.format(c[i],a[i],b[i]))
'''              

#to find the missing no.
'''
b=[4,5,7,8,8,9,11,14]
for i in range(min(b),max(b)):
    if i not in b:
        print('the missing nos are ',i)
        '''
#to find the missing no with difference of 2
'''
a=[4,6,10,12,16,18,22]
for i in range(min(a),max(a),2):
    if i not in a:
        print('the missing',i)
        '''


#to print the 10th prime no.

count=0
for i in range(2,300):
    for j in range(2,i):
        if (i%j)==0:
            break
    else:
            count=count+1
            print(count)
            if count==10:
                print(i)
                break
             
           
             
            
          
          
        
    
