from random import randint
contagem = ('zero', 'um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while True:
    b = int(input('digite um numero entre 0 e 20: '))
    if b > 20:
        print('numero invalido, tente novamente.\n')
    else:
        print(contagem[b])
        break
