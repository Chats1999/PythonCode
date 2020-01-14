'''
a=input('enter a name')
b=input('enter the second name')
d=['Friends','Love','Affection','Marriage','Enemy','Sibling']
c=list(a)
b=list(b)

for i in a:
    for j in b:
        print(i,j)
        if i==j:
            c.remove(i)
            b.remove(j)
            break
print(c)
print(b)
length=len(c)+len(b)
print(length)
ans=length%len(d)
print([d][ans-1])
'''
        
f=open('Chaith.txt','r')
print(f.read())

