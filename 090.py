aluno = {}
lista = []

aluno['nome'] = str(input('qual seu nome? '))
aluno['media'] = float(input(f'media de {aluno['nome']}: '))
if aluno['media'] < 6:
    situação = 'REPROVADO'  
else:
    situação = ' APROVADO'
aluno['situação'] = situação
for i, v in aluno.items():
    print(f'{i} é igual a {v}')