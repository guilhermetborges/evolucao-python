def fatorial(num=1, show=False):
    """função para calcular uma fatorial"""
    f=1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ',end='')
            else: print(' = ', end='')
        f *= c
    return f

calcularfat = int(input('digite um numero para calcular fatorial: '))
print(fatorial(calcularfat))