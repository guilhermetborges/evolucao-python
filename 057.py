s = str(input('qual seu sexo: [M|F]   ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('dados invalidos,por favor digite novamente: [M|F] ')).strip().upper()[0]
    
print('sexo {} registrado'.format(s))
print('FIM')