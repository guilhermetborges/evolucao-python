from datetime import date
sexo = str(input('''
                 masculino[M]
                  feminino[F]
                 qual seu sexo: ''')).lower()

nasc = int(input(' em que ano você nasceu? '))

atual = date.today().year

prazo1 = 18-(atual - nasc)
prazo2 =  (atual-nasc) - 18
if sexo == 'f':
     print('você não deve se alistar')
elif sexo == 'm':
     print('você deve se alistar confira os prazo abaixo')
else:
     print('ocorreu um erro,tente novamente')

if sexo == 'm'and nasc + 18 > atual:
    print('você ainda vai se alistar para o serviço militar')
elif sexo == 'm' and nasc + 18 == atual:
    print('você deve se alistar no serviço militar JÁ')
elif sexo == 'm' and nasc + 18 < atual:
    print('já passou da hora de se alistar!')

if sexo == 'm' and nasc + 18 > atual:
       print('você deve se alistar em {} anos'.format(prazo1))
elif sexo == 'm' and nasc + 18 < atual:
     print('você passou {} anos do prazo'.format(prazo2))
     
    