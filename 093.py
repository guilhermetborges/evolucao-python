
player = {}
goalsPerGame = []
totalGols = 0
player['jogado'] = str(input('nome do jogador: '))
partidas = int(input(f'quantas partidas {player["jogado"]} jogou? '))
for c in range(partidas):
    gols = int(input(f'Quantos gols fez na partida {c+1}: '))
    totalGols += gols
    goalsPerGame.append(gols)

player['gols'] = goalsPerGame
player['total De Gols'] = totalGols

print('=-='*11)
for valores, jogador in player.items():
    print(f'O campo {valores} tem valor {jogador}')
print('-=-'*5)
print(f'O jogador {player["jogado"]} jogou {partidas} partidas\nCom um total de {player["total De Gols"]} gols')
for i, gols in enumerate (goalsPerGame):
    print(f'na partida {i+1} fez {gols} gols.')


