print('=-=-=BEM VINDO AO BANCO DEV=-=-=')
valorSaque = int(input('valor do saque:R$  '))
total = valorSaque
ced = 200
totalCed = 0
while True:
    if total >= ced:
        total -= ced
        totalCed +=1
    else:
        if totalCed > 0:
            print(f'total de {totalCed} cédulas de R${ced}')
        if ced == 200:
            ced = 100
        if ced == 100:
            ced = 50
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totalCed = 0
        if total == 0:
            break
