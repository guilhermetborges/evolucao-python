from random import randint
computador = randint(1,10)
tentativas = 0
nmr = 0
while nmr != computador:
    nmr = int(input('escolha um numero de 1 a 10: '))
    tentativas += 1
    if nmr > computador:
        print('menos... tente novamente')
    elif nmr < computador:
        print('mais... tente novamente')
print('parabéns você acertou o número em {} tentativas'.format(tentativas))