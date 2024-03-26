r1 = float(input('reta 1: '))
r2 = float(input('reta 2: '))
r3 = float(input('reta 3: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('pode formar um triangulo ', end='')
    if r1 == r2 and r2 == r3:
         print('Equilátero')
    if  r1 == r2 != r3 or r1 == r3 != r2  or r2 == r3 != r1:
         print(' ISÓSCELES')
    if r1 != r2 != r3 != r1:
        print('ESCALENO')
else:
    print('não pode formar um triângulo')


