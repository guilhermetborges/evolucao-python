t1 = int(input('digite o primeiro termo de uma p.a: '))
razao = int(input('razão da PA: '))
termo = t1
contador = 1
total = 0 
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(' {} > '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar mais? '))
print('FIM\n')
print('O programa utilizou ao todo {} termos '.format(total))