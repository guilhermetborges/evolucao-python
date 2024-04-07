valores = []
s = 0
while True:
    valor = int(input('digite um valor: '))
    valores.append(valor)
    while True:
        continuar = str(input('quer continuar? S|N: ')).strip().upper()
        if continuar not in 'SN':
            print('opção invalida, responda novamente')
        else : break
    if continuar == 'N':
        break
print(f'você digitou {len(valores)} elementos!')
valores.sort(reverse=True)
print(f'os valores em ordem decrescente são {valores}')


if 5 not in valores:
    print('o valor 5 não foi encontrado')
else:
    for valor in valores:
        if valor == 5:
            s += 1
    print(f'o valor 5 foi encontrado e apareceu {s} vezes')