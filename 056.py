maior = 0
nomedovei = ''
idade = 0
menosde20 = 0
for c in range(1,5):
    print('===={}ª PESSOA===='.format(c))
    nome = str(input('nome da {}ª pessoa: '.format(c)))
    idad = int(input('idade da {}ª pessoa: '.format(c)))
    sexo = str(input('sexo [M/F] : ')).upper().strip()
    idade += idad
    media = idade/4
    if c == 1 and sexo == 'M':
        maior = c
        nomedovei = nome
    else:
        if idad > maior and sexo == 'M':
            maior = idad
            nomedovei = nome
        
    if sexo == 'F' and idad < 20:
        menosde20 += 1
print('\nA media da idade do grupo é {} anos\n'.format(media))
print('O homem mais velho tem  {} anos e se chama {}\n'.format(maior,nomedovei))
print('{} mulheres tem menos de 20 anos.'.format(menosde20))