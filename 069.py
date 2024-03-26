maiorde18 = homem = mulhermenosde20 = 0
sexo = ''
while True:
    idade = int(input('digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('digite seu sexo [M/F]: ')).strip().upper()[0]
    print('=-' * 10) 
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('você que continuar [S/N]: ')).strip().upper()[0]
    print('=-=' * 10)
    if idade >= 18:
        maiorde18 +=1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulhermenosde20 += 1
    if continuar == 'N':
        print(f'''total de pessoas com mais de 18 anos: {maiorde18}
total de homens cadastrados: {homem}
total de mulheres com menos de 20 anos: {mulhermenosde20}''')
        break
