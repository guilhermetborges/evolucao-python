lanche = ['hamburguer','coca cola','combo','picole','suco','hot-dog','pizza']
cardapioNum1 = lanche[:]
lanche[2] = 'combo com fritas'
lanche.insert(0,'CARDAPIO')
lanche.append('pirulito')
del lanche[7]
lanche.pop(3)
lanche.remove('picole')
lanche.insert(1, 'Fritas')
print(lanche)
print(cardapioNum1)

valores = list(range(1,11))
for c in range(10):
    v1 = int(input('digite um valor: '))
    valores[c] = v1
    valores.sorted
for p, v in enumerate(valores):
    print(f' na posição {p+1} está o valor: {v}!')
#valores.sort() #para ordenar em ordem decrescente = valores.sort(reverse=True)
#print(valores)

