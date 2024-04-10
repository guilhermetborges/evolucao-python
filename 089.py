aluno = []
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota 1 : '))
    nota2 = float(input('nota 2 : '))
    media = (nota1 + nota2) /2
    aluno.append([nome,[nota1,nota2],media])

    while True:
        resp = str(input('quer continuar [S|N]')).strip().upper()
        if resp not in 'SN':
            print('resposta invalida tente novamente')
        else: break


    if resp == 'N':
        break

print(f'{"No.": <5}{"NOME":<12}{"MEDIA":>8}{"SITUAÇÃO":>15}')
print('_'*52)

for i, a in enumerate(aluno):
    if a[2] <= 5:
        situação = 'REPROVADO'
    elif a[2] > 5 and a[2]<6:
        situação = 'RECUPERAÇÃO'
    else:
        situação = 'APROVADO'

    
    print(f'{i:<4}{a[0]:<12}{a[2]:>8.1f}{situação:>15}')

while True:
    print('-='*22)
    opc = int(input('mostrar nota de qual aluno?  (999 interrompe)'))

    if opc == 999:
        break

    if opc <= len(aluno) - 1:
        print(f'notas de {aluno[opc][0]} são {aluno[opc][1]}')
print('-='*12)
