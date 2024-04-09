dados = []
pessoas = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1]< men:
            men = dados[1]

    while True:
        cont = str(input('quer continuar? [S|N] ')).strip().upper()
        if cont not in 'SN':
            print('opção invalida tente novamente')
        else: break
    pessoas.append(dados[:])
    dados.clear()
    if cont == 'N':
        break
print(f'ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi {mai} KG, peso de ',end='')
for p in pessoas:
    if p[1]== mai:
        print(f'{p[0]}')
print(f'o menor peso foi de {men} KG, peso de ',end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}')