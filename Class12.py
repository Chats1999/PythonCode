#to construct a keypad using dictionary

aw=int(input('enter a value'))
a=int(input('enter a value'))

Ca={1:'1',2:['a','b','c'],3:['d','e','f'],4:['g','h''i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}

    
if aw==9 or aw==7:
    
        if a%4==1:
            print(Ca[aw][0])
        elif a%4==2:
            print(Ca[aw][1])
        elif a%4==3:
            print(Ca[aw][2])
        elif  a%4==4:
            print(Ca[aw][3])
            
else:    
    if a>3:
            if a%3==1:
                print(Ca[aw][0])
            elif a%3==2:
                print(Ca[aw][1])
            elif a%3==3:
                print(Ca[aw][2])
            
            
        
    else:     
        print(Ca[1][1])
        

#to construct a keypad using dictionary
aw=int(input('enter a value'))
a=int(input('enter a value'))

Ca={1:'1',2:['a','b','c'],3:['d','e','f'],4:['g','h''i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}

    
if aw==9 or aw==7:
    print(Ca[aw][a%4-1])
else:
    if a>3:
        print(Ca[aw][a%3-1])
    else:
     print(Ca[aw][a])
    
