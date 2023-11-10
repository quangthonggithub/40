a=int(input('Side 1:'))
b=int(input('Side 2:'))
c=int(input('Side 3:'))
if a==b and a!=c:
    print('An isosceles triangle')
elif b==c and b!=a:
    print('An isosceles triangle')
elif c==a and c!=b:
    print('An isosceles triangle')
elif a==b or a==c or c==a:
    print('An equilateral triangle')
else:
    print('A scalene triangle')
