listaDePreços = ('uma duzia de ovos', 6.99,
                 'vinho', 19.99,
                 'azeite',5.99, 
                 'queijo', 9.99, 
                 'margarina', 2.50)
print(f'{"MERCADO DEV":-^40}')
for c in range(0, len(listaDePreços)):
    if c % 2 == 0:
        print(f'{listaDePreços[c]:.<30}',end=' ')
    else:
        print(f'R${listaDePreços[c]:>3.2f}')