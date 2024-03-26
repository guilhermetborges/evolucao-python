maiormenor = []
for p in range(1, 6):
    peso = float(input('peso da {}ª pessoa: '.format(p)))
    maiormenor.append(peso)
print(f'o maior peso é {max(maiormenor)} e o menor peso é {min(maiormenor)}')