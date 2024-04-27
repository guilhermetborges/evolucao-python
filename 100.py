from random import randint
from time import sleep
def sorteia():
    print('Gerando numeros aleatorios...')
    sleep(0.5)
    print('=-='*10)
    lst = []
    for _ in range(5):
        numeros = randint(1,500)
        print(numeros)
        sleep(0.5)
        lst.append(numeros)
    print('=-='*10)
    return lst







def somapar():
    numeros = sorteia()
    somapares = 0
    somaimpar = 0
    for num in numeros:
        if num % 2 == 0:
            somapares += num
        else:
            somaimpar += num
    print(f'A soma dos numeros pares é {somapares}\nA soma dos numeros impares é {somaimpar}')




somapar()