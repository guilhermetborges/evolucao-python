from datetime import date

nasc = int(input('em que ano você nasceu? '))
atual = date.today().year

if (atual - nasc) <= 9:
    print('MIRIM')
elif (atual - nasc) <= 14:
    print('INFANTIL')
elif (atual - nasc) <= 19:
    print ('JUNIOR')
elif (atual - nasc) == 20:
    print('SÊNIOR')
else:
    print('MASTER')