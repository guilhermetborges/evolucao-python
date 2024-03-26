from math import factorial
nmr = int(input('digite um numero: '))
print('\ncalculando fatorial de {} : '.format(nmr), end='')
c = nmr 
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(' {} '.format(f))
fac = int(input('digite um numero pra calcular o fatorial\n'))
print('{}! = {}'.format(fac,factorial(fac)))

numero = int(input('digite um numero: '))
y = 1
for x in range (numero, 0, -1):
    print('{}'.format(x), end='')
    print(' x ' if x > 1 else ' = ', end='')
    y *= x
print('{}'.format(y), end='')

