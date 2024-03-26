from datetime import date
ano = int(input('digite um ano: , coloque 0 para analisar o ano atual)'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é BISSEXTO\033[33;42m'.format(ano))
else:
    print('o ano {} não é BISSEXTO\033[31;41m',format(ano))