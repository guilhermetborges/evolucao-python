
par = impar = 0
while c != 0:
    c = int(input('digite um numero: '))
    if c != 0:
        if c % 2 == 0:
            par += 1
        else:
            impar += 1
print('o numero de pares foi {} e de impares foi {}'.format(par,impar))