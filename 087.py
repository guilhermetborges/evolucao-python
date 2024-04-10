matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'digite um valor para [{l+1},{c+1}] :  '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end='')
        if matriz[l][c] % 2 ==0:
            spar += matriz[l][c]
    print()
print('=-'*30)
print(f'a soma dos valores pares é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'a soma das colunas é {scol}')

mai = max(matriz[1])  # Encontra o maior valor da segunda linha
print(f'o maior valor da segunda linha é {mai}')