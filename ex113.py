def leiadinheiro(msg):
    while True:
        try:
            entrada = float(input(msg))
        except(ValueError,TypeError):
                print('\033[0;31mERRO, FOI DIGITADO UM VALOR INVALIDO!\033[m')
                continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO, ENTRADA DE DADOS INTERRONPIDA PELO USUARIO!\033[m')
        else:
            return float(entrada)

def leiaint(msg):
    while True:
        try:
            entrada = int(input(msg))
        except(ValueError,TypeError):
            print('\033[0;31mERRO, FOI DIGITADO UM NUMERO INVALIDO!\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mERRO, ENTRADA DE DADOS INTERRONPIDA PELO USUARIO!\033[m')
        else:
            return entrada