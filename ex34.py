a=int(input('Enter integer:'))
if a%2==0 and a>0 :
    print('The integer is even')
elif a%2!=0 and a>0:
    print('The integer is odd')
elif a%-2==0 and a<0:
    print('The integer is even')
elif a%-2!=0 and a<0:
    print('The integer is odd')
