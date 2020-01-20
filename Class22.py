#to add the value of only dosa by 15.5 and to replace the old value by it
f=open('chaith.txt','r')
a=open('Chaithu.txt','a')
findword='dosa='
for i in f:
    for j in i.split():
        if findword in j:
            w=j.split('=')[1]
            x=float(w)+15.5
            new=findword+str(x)
            a.write(new+' ')
            
            

        else:
            a.write(j+' ')
    a.write('\n')
            
            
a.close()           
                
