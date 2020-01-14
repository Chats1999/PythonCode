
#to read the text document

f=open('Chaith.txt','r')
print(f.read())

#to read the words in the text document

f=open('Chaith.txt','r')
for i in f:
    for j in i.split():
        print(j)
        
#to write in the text document
a=open('Chaith.txt','w')
a.write('\n Hi Cutie')
a.close()

#to append something into the text document

a=open('Chaith.txt','a')
a.write('\nYou are Cute')
a.close()

# to write username and password into the text document until we write exit
while True:
    user=input('enter a username')
   
    if user=='exit':
        break
    password=input('enter a password')
    a=open('Chaith.txt','a')
    a.write('\n user {}: password {}'.format(user,password))
a.close()

#to replace bita by tata and then to paste into a new document
a=open('Chaith.txt','r')
x=open('Chaithu1.txt','a')
for i in a:
    
    if 'bita' in i:
        i=i.replace('bita','tata')
        
        x.write(i)
    else:
        x.write(i )
x.close()        
                   
                      
        
    
