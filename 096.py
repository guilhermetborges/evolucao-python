def area():
    largura = float(input('digite a largura: '))
    comprimento = float(input('digite o comprimento: '))
    print(f'a area do seu terreno de {largura}x{comprimento} é de {largura*comprimento}m2')



def volume():
    largura = float(input('digite a largura: '))
    comprimento = float(input('digite o comprimento: '))
    areadabase = largura *comprimento
    altura = float(input('digite a altura: '))
    print(f'{areadabase*altura}')




area()
volume()