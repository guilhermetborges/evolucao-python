from utilidadecev import moeda

def leiadinheiro(msg):
    while True:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isnumeric():
            break
        else:
            print('\033[0;31mERRO,DIGITE UM NUMERO VALIDO!\033[m')
        
    return float(entrada)