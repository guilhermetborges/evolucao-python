n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
n4 = int(input('digite um numero: '))
tupla = (n1,n2,n3,n4)
soma = 0
totalPar = []
for cont in range(0 , len(tupla)):
    if tupla[cont] == 9:
        soma +=1

print(f'você digitou os valores {tupla}')
if 9 in tupla:
    print(f'o valor 9 apareceu {soma} vezes')
if 3 in tupla:
    pos = tupla.index(3) + 1
    print(f'o numero 3 está na posição {pos}')
else:
    print('a variavel não tem numero 3')
if n1 % 2 == 0:
    totalPar.append(n1)
if n2 % 2 == 0:
    totalPar.append(n2)
if n3 % 2 == 0:
    totalPar.append(n3)
if n4 % 2 == 0:
    totalPar.append(n4)
if totalPar == []:
    print('nenhum numero é par')
print(f'Os numeros pares foram {totalPar}')
print('''\n       proximo teste\n 
=-=-=-=-=-=-=-=-====-=-=-=-=-=''')

num = (int(input('digite um numero: ')),
       int(input('digite um numero: ')),
       int(input('digite um numero: ')),
       int(input('digite um numero: ')))
print(f'você digito os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vez.')
if 3 in num:
    pos2 = num.index(3) + 1
    print(f'o numero 3 está na posição {pos2}')
print('os numeros pares foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')