from random import randint
from time import sleep 
itens = ('pedra', 'papel','tesoura')
computador = randint(0, 2)
jogada = computador

print('''Sua jogada: 
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')

joga = int(input('Qual é a sua jogada? '))
print(jogada)

print('JO')
sleep(0.6)
print('KEN')
sleep(0.3)
print('PO')
sleep(0.5)

print('-=' * 16)
if joga == 0:
    if jogada == 1:
        print('''  DERROTA
O computador jogou PAPEL ''')
    elif jogada == 0:
        print('''   EMPATE 
O computador jogou PEDRA ''')
    elif jogada == 2:
        print('''  VITÓRIA!!!
 O computador jogou TESOURA''')
elif joga == 1:
    if jogada == 0:
        print('''VITÓRIA!!!
O computador jogou PEDRA''')
    elif jogada == 1:
        print('''EMPATE
 O computador jogou PAPEL''')
    elif jogada == 2:
        print(''' DERROTA
O computador jogou TESOURA''')
elif joga == 2:
    if jogada == 0:
        print('''DERROTA
O computador jogou PEDRA''')
    elif jogada == 1:
        print('''VITÓRIA!!!
O computador jogou PAPEL''')
    elif jogada == 2:
        print(''' EMPATE
 O computador jogou TESOURA''')
else:
    print('Opção inválida. Tente novamente.')

print(('-=' * 16))