
from random import randint
from time import sleep
nmr = v = 0
jmaq = ''
print('=-=' * 7)
print('jogue ate perder')
print('=-=' * 7)
while True:
    jogada = str(input("IMPAR ou PAR: ")).upper().strip()
    if jogada == "IMPAR":
        (sleep(1))
        print("COMPUTADOR: PAR")
        jmaq = "PAR"
    elif jogada == "PAR":
        (sleep(1))
        print("COMPUTADOR: IMPAR")
        jmaq = "IMPAR"
    else:
        print('erro, tente novamente')
    print('=-='*10)
    if jogada == 'IMPAR' or jogada == 'PAR':
        nmr = int(input('digite um numero: '))
        computador = randint(0,10)
        sleep(1)
        print(f'computador jogou :{computador}')
        sleep(0.5)
        print(f'{nmr} + {computador} = {nmr+computador}')
        res = (nmr + computador) % 2
        print ('=-='*10)
    if jmaq == "PAR" and res == 0:
        sleep(1)
        print('RESULTADO = PAR\nVOCÊ PERDEU')
        d =  1
        break
    elif jmaq == 'PAR' and res == 1:
        sleep(1)
        print('RESULTADO = IMPAR\n PARABÉNS! VOCÊ VENCEU')
        v += 1
    if jmaq == "IMPAR" and res == 1:
        sleep(1)
        print('RESULTADO = IMPAR \nVOCÊ PERDEU')
        d = 1
        break
    elif jmaq == 'IMPAR' and res == 0:
        sleep(1)
        print('RESULTADO = PAR\n PARABÉNS! VOCÊ VENCEU')
        v +=1
print(f'Acabou o numero de vitorias foram {v}')