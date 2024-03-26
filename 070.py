produto = []
total = total1000 = 0
while True:
    nomeProduto = str(input('qual produto você comprou? ')).strip()
    valorProduto = int(input('qual o valor do produto? '))
    produto.append(valorProduto)
    if valorProduto > 1000:
        total1000 +=1
    if valorProduto == min(produto):
        menorValor = nomeProduto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('você deseja continuar [S/N]: ')).strip().upper()[0]
    total += valorProduto
    if continuar == 'N':
        break
print(f'O valor total gasto foi {total}')
print(f'A quantidade de produtos que custaram mais que 1000 R$ foram {total1000}')
print(f'O produto mais barato foi {menorValor}, que custa {min(produto)}R$')