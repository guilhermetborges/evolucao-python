nmr = total = soma = 0
nmr = int(input('digite um numero, [999] para parar: '))
while nmr != 999:
    total += 1
    soma += nmr
    nmr = int(input('digite um numero, [999] para parar: '))
print('você digitou {} vezes e a soma dos numeros foi {}'.format(total,soma))
