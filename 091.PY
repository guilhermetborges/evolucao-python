from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador_1': randint(1,6),
    'jogador_2': randint(1,6),
    'jogador_3': randint(1,6),
    'jogador_4': randint(1,6)
}
ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-='*8)
print('VOCÊ tem DADO em casa? ')
print('=-='*8)
for jogador, jogada in jogo.items():
    print(f'o {jogador} jogou: {jogada}')
    sleep(0.8)
#ordem de vencedores
for colocaçao, jogada in enumerate(ranking):
    print(f'O {colocaçao+1}o lugar é {jogada[0]} com {jogada[1]} pontos. ')
    sleep(0.8)