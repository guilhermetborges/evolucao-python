from time import sleep
valores = []
c = 0
while True:
    num = int(input('digite um valor: '))
    if num not in valores:
        valores.append(num)
        sleep(0.5)
        print('valor adicionado com sucesso...')
    else:
        print('valor duplicado!')
    while True:
        continuar = str(input('quer continuar [S|N]: ')).strip().upper()
        if continuar == 'N' or continuar == 'S':
            break
        else:
            print('opção invalida , tente novamente')
    if continuar == 'N':
        break
print('-='*25)
valores.sort()
print(valores)