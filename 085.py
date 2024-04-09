lista = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'digite o {c}o. valor: '))
    if valor %2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'os numeros pares da lista são {lista[0]}\nOs numeros impares são {lista[1]}')