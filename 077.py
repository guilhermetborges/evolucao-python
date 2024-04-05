palavras = 'AMEM', 'AGENTE', 'PROFESSOR', 'ESTUDANTE','MODELO','TORCEDOR','AMIGO'
for c in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[c]} temos ',end='')
    for letra in palavras[c]:
        if letra in 'AEIOU':
            print(letra, end=' ')