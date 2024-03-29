n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
n4 = int(input('digite um numero: '))
tupla = (n1,n2,n3,n4)
soma = totalPar =0
for cont in range(0 , len(tupla)):
    if tupla[cont] == 9:
        soma +=1

print(f'você digitou os valores {tupla}')
if 9 in tupla:
    print(f'o valor 9 apareceu {soma} vezes')
if 3 in tupla:
    pos = tupla.index(3) + 1
    print(f'o numero 3 está na posição {pos}')
if n1 % 2 == 0:
    totalPar += 1
if n2 % 2 == 0:
    totalPar += 1
if n3 % 2 == 0:
    totalPar += 1
if n4 % 2 == 0:
    totalPar += 1
print(f'O total de numeros pares foi {totalPar}')


