def mostralinha(msg):
    print('=-='*20)
    print(msg)
    print('=-='*20)

#mostralinha(f'{"sistemas de alunos":^50}')

def soma(a, b):
    s = a + b
    print(s)

#soma(2,5)

def somaInt():
    a = int(input('N1: '))
    b = int(input('N2: '))
    print(a+b)

#somaInt()

def contador(*num):
    tot = 0
    for valores in num:
        tot += valores
    print(tot)

contador(2,3,4)