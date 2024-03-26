num = int(input('digite um numero: '))

print('''escolha uma das bases para converção:
      [1] converter para binário
      [2] converter para octal
      [3] converter para hexadecimal ''')
opção = int(input('opção: '))

if opção == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida')