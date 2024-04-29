from time import sleep

def msg (mensagem):
    print('~'*(len(mensagem) + 4))
    print(f'  {mensagem}')
    print('~'*(len(mensagem)+ 4))


def contador(i, f, p):
    msg(f'contagem de {i} ate {f} de {p} em {p}')
    sleep(1.2)
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont -= p
    print()
    print('====FIM====')



contador(1, 10 ,1)
contador(10, 0, 2)
inicio = int(input('inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)