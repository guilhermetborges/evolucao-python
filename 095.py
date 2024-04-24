time = []

while True:
    player = {}
    player['jogador'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {player["jogador"]} jogou? '))
    gols_por_partida = []
    totalGols = 0

    for c in range(partidas):
        gols = int(input(f'Quantos gols {player["jogador"]} fez na partida {c+1}: '))
        totalGols += gols
        gols_por_partida.append(gols)

    player['gols'] = gols_por_partida
    player['total de gols'] = totalGols
    time.append(player.copy())

    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar != 'S':
        break

print('=-=' * 15)
print(f'{"cod":<5}{"nome":<10}{"gols":<15}{"total":<10}')
print('=-=' * 15)

for i, jogador in enumerate(time):
    print(f'{i:<5}{jogador["jogador"]:<10}{str(jogador["gols"]):<15}{jogador["total de gols"]:<10}')

while True:
    busca = int(input('Mostrar dado de qual jogador? [999 para parar]'))
    if busca == 999: break
    if busca >= len(time):
        print(f'Não existe jogador com codigo {busca}')
    else:
        print(f'levantamento do jogador {time[busca]["jogador"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('=-='*10)
print('ENCERRADO')