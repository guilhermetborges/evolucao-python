nmr=soma=total = 0
numeros = []
cont = 'S'
while cont == 'S':
    nmr = int(input('digite um numero: '))
    cont = str(input('você que continuar? [S|N] :\n')).strip().upper()
    numeros.append(nmr)
    total += 1
    soma += nmr
    media = soma/total
    if cont == 'N':
        print('o total de valores digitados foi {} a media entre os valores digitados foi {:.1f} e o maior numero foi {} e o menor foi {}'.format(total,media,max(numeros),min(numeros)))
    elif cont not in 'NS':
        print('comando desconhecido,tente novamente.')
    