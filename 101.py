import datetime
def voto(ano):
    """
    verificação da obrigatoriedade do voto
    """
    atual = datetime.datetime.now().year
    idade = atual - ano
    if idade < 16:
        situaçao = (f'com {idade} anos: NÃO VOTA')
    elif idade >= 16 and idade < 18:
        situaçao =(f'com {idade} anos: VOTO OPCIONAL')
    elif idade >= 18 and idade < 65:
        situaçao =(f'com {idade} anos: VOTO OBRIGATORIO')
    elif idade >= 65:
        situaçao =(f'com {idade} anos: VOTO OPCIONAL')

    return situaçao
nasc = int(input('em que ano voce nasceu: '))

print(voto(nasc))