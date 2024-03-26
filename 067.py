cont = 0
while True:
    print('--'*15)
    tabuada = int(input('quer ver a tabuada de qual valor? '))
    print('--'*15)
    if tabuada < 0:
          break
    for cont in range (0,10):
            cont += 1
            print(f'{tabuada} x {cont} = {tabuada*cont}')
print('ACABOU')    