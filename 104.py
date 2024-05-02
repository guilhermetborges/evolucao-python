def leiaint(x):
    print('=-='*7)
    print(x,end='')
    while True:
        num = input()
        if num.isnumeric():
            break
        else:
            print('\033[0;31mERRO!DIGITE UM NUMERO VALIDO!\033[m')
    return num
        
n = leiaint('digite um  numero: ')
print(f'você acabou de digitar o numero {n}')