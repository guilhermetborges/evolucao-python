cont = cont2 = 0
s = 0
while True:
    cont2 += 1
    print(cont2,' > ', end='')
    ln = int(input('digite um numero : 999 para parar: '))
    if ln == 999:
        break
    s += ln
    cont += 1
print(f'A soma é {s} em {cont} numeros digitados')