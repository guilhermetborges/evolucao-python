pessoas = [['Pedro',25,1.78],['João', 32,1.66],['lucas', 33,1.65]]
#pessoas.append(dados[:])
print(pessoas[0])
print(pessoas[1][2])
for p in pessoas:
    print(f'olá {p[0]}, você tem {p[1]} anos e {p[2]} de altura')
sugestões = []
lista = []
for c in range(0,2):
    lista.append(str(input('indique um prato para o cardapio: ')))
    lista.append(int(input('digite o valor que você sugere paraeste prato: ')))
    sugestões.append(lista[:])
    lista.clear()
print(f'os pratos sugeridos foram {sugestões[0][0]} e {sugestões[1][0]}')

