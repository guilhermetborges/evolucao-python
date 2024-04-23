pessoa = {}
galera = []
soma = media =  0
while True:
    pessoa.clear()
    pessoa['pessoa' ] = str(input('Nome: '))
    
    while True:
        pessoa['sexo'] = str(input('sexo: [M|F] ')).strip().upper()
        if pessoa['sexo'] not in 'MF':
            print('Comando invalido, digite novamente')
        else: break
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        continuar = str(input('quer continuar? [S||N] ')).strip().upper()
        if continuar not in 'SN':
            print('Comando invalido, digite novamente')
        else: break
    if continuar == 'N':
        break
print(galera)
print(f'ao todo temos {len(galera)} pessoas cadastradas.')
media = soma/len(galera)
print(f'A media de idade é de {media:4.1f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p['pessoa']} ',end='')
print('Lista de pessoas que estão acima da media: ', end='')
for p in galera:
    if p['idade'] > media:
        print(f'   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()