def ficha(jogador=str,gols=int):
    """"
    ficha mostra a relação jogador/gols
    """
    if jogador == '' or jogador == ' ':
        jogador = '<desconhecido>'
    
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'o jogador {jogador} fez {gols} gols.')
    

jogador1 = str(input('qual o nome do jogador: '))
gols1 = input('quantos gols o jogador marcou: ')
ficha(jogador1,gols1)