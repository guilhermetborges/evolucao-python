from time import sleep
def maior(*valor):
    print('-='*20)
    print('ANALISANDO OS VALORES PASSADOS...')
    print('-='*20)
    sleep(1)
    print('os valores são: ', end='')
    for valores in valor:
        print(valores, end='  ')
    print(f' um total de {len(valor)} ao todo.')
    print(f'o maior valor informado foi {max(valor)}')

maior(2,3,4,3)