a=int(input('Enter decibel level:'))
if a==130:
    print('Jackhammer')
elif a==106:
    print('Gas lawnmower')
elif a==70:
    print('Alarm clock')
elif a==40:
    print('Quite room')
elif 106<a<130:
    print('Between Jackhamme and Gas lawnmower')
elif 70<a<106:
    print('Between Gas lawnmower and Alarm clock')
elif 40<a<70:
    print('Between Alarm clock and Quite room')
else:
    if 0<a<40:
        print('Noise level is very low')
    if a>130:
        print('Noise level is very loud')
    if a==0:
        print('No sound')