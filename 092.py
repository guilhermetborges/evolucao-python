from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('data de nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['casteira De trabalho'] = int(input('carteira de trabalho: (0| não tem) '))
if cadastro['casteira De trabalho'] == 0:
    print('=-='*8)
else:
    cadastro['contratação'] = int(input('ano de contratação: '))
    cadastro['salario'] = int(input('Salario: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - datetime.now().year)
print('-='*25)
for cadastro, valores in cadastro.items():
    print(f'o valor de {cadastro} é {valores}') 