from time import sleep
valores = []
teste = []
testeimpar = []
c = 0
while True:
    num = int(input('digite um valor: '))
    valores.append(num)
    sleep(0.5)
    print('valor adicionado com sucesso...')
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
print(f'a lista completa é {valores}')
pares  =valores [:]
impares = valores[:]
pares = [num for num in pares if num % 2 == 0]
impares =[num for num in impares if num % 2 != 0]
print(f'os numeros pares da lista são {pares}!\nOs numeros impares são {impares}!')

for i , v in enumerate(valores):
    if v % 2 == 0:
        teste.append(v)
    else:
        testeimpar.append(v)
print(f'pares: {teste}, impares: {testeimpar}')