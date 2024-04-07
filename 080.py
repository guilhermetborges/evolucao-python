valor = []
for v in range (0,5):
    n = int(input('digite um valor: '))
    if v == 0 or n > valor[-1]:
        valor.append(n)
    else:
        pos = 0
        while pos < len(valor):
            if n <= valor[pos]:
                valor.insert(pos, n)
                print(f'adicionado na posição {pos} da lista')
                break
            pos+=1
print(valor)