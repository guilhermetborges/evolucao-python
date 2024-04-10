from random import randint
print('--'*16)
print('JOGUE NA MEGA SENA')
print('--'*16)
lista = []
jogos = []
quant = int(input('quantos jogos você quer que eu sorteie: '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont == 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total +=1
print('=='*3,f'SORTEANDO {quant} JOGOS', ' =='*3)
print(f'os jogos sorteados foram :')
for i , l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')