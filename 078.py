valores = list(range(0,5))
for p, v in enumerate(valores):
    valor = int(input(f'digite um valor para posição {p+1}: '))
    valores[p] = valor

maior = max(valores)
menor = min(valores)

posicoes_maior = [i + 1 for i, v in enumerate(valores) if v == maior]
posicoes_menor = [i + 1 for i, v in enumerate(valores) if v == menor]

print(f'os valores digitados são {valores}\nO maior valo digitado foi: {max(valores)} ', end='') 
if len(posicoes_maior) == 1:
     print(f'na posição {" ,".join(map(str,posicoes_maior))}')
else: 
     print(f'nas posições {", ".join(map(str, posicoes_maior))}')

print(f'O menor valor digitado foi: {min(valores)} ', end='')
if len(posicoes_menor) == 1:
     print(f'na posiçao {", ".join(map(str,posicoes_menor))}')
else:
    print(f'nas posições {", ".join(map(str,posicoes_menor))}')