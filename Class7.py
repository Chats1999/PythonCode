#car started and stopped print
'''
instr=input('enter a command')
if instr=='start':
    print('the car started')
elif instr=='stop':
    print('the car stopped')
else:
    print('didnt understand command')
'''
#to get output printed even if given in uppercase command
'''
instr=input('enter a command').lower()
if instr=='start':
    print('the car started')
elif instr=='stop':
    print('the car stopped')
else:
    print('didnt understand command')
'''
#infinite loop
'''
instr=input('enter a command')
while True:
if instr=='start':
    print('the car started')
elif instr=='stop':
    print('the car stopped')
else:
    print('didnt understand command')

'''
# to print already started and already stopped
'''
started=0
while True:
 instr=input('enter a command')
 if instr=='start':
    if started==1:
      print('the car already started')
    else:
      print('the car started')
      started=1
    
 elif instr=='stop':
        if started==0:
          print('the car already stopped')
        else:
          print('the car stopped')
          started=0
 elif instr=='exit':
        break
 elif instr=='help':
        print('''start---to start the car
stop---to stop the car
help---to help menu
exit---to exit''')
 else:
    print('didnt understand command')
  '''
#to print already started and already stopped using true and false
'''
started=False
while True:
 instr=input('enter a command')
 if instr=='start':
    if started:
      print('the car already started')
    else:
      print('the car started')
      started=True
    
 elif instr=='stop':
        if not started:
          print('the car already stopped')
        else:
          print('the car stopped')
          started=False
 elif instr=='exit':
        break
 elif instr=='help':
        print('''start---to start the car
stop---to stop the car
help---to help menu
exit---to exit''')
 else:
    print('didnt understand command')


    '''
#to print weight in pounds and kg
'''
name=input('enter the name')
weight=int(input('enter the weight'))
a=input('enter kg or l')

if a=='l':
 ans=weight*float(0.4535)
 print('Hi' ,name,'your weight in kg is',ans) 
if a=='kg':
    ans=weight*float(2.20462)
    print('hi',name,'your weight in pounds is',ans)
'''
#to check anagram or not
    '''
#to check if anagram or not
a=list('listen')
b=list('silent')
a.sort()
b.sort()
for i in range(len(a)):
        if a[i]==b[i]:
         print('it is an anagram')
         break
        else:
            print('not an anagram')
            break
