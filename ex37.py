a=int(input('Number of sides:'))
if a<3:
    print('This shape is not available')
elif a>10:
    print('This shape is not support')
else:
    if a==3:
        print('Triangle')
    if a==4:
        print('Quadrilateral')
    if a==5:
        print('Pentagon')
    if a==6:
        print('Hexagon')
    if a==7:
        print('Heptagon')
    if a==8:
        print('Octagon')
    if a==9:
        print('Hexagon')
    if a==10:
        print('Decagon')
 
    