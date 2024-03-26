print('-=-'*12)
print('=-='*2,'Sequencia de Fibonacci','=-='*2)
print('-=-'*12)
qtdetermos = int(input('quandos termos você quer mostrar? \n'))
print('~'*30)
t1 = 0
t2 = 1
cont = 3
print(f'{t1} > {t2}',end='')
while cont <= qtdetermos:
    t3 = t1 + t2
    cont += 1
    print(f' > {t3} ', end='')
    t1 = t2
    t2 = t3
print('> FIM', end='')
