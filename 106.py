def exibir_mensagem(mensagem):
    print('~' * (len(mensagem) + 4))
    print(f'  {mensagem}')
    print('~' * (len(mensagem) + 4))

def ajuda(com):
    help(com)
while True:
    exibir_mensagem('SISTEMA DE AJUDA PyHELP')
    comando = input("Função ou biblioteca > ").strip()
    if comando == 'fim':
        break
    else: ajuda(comando)

exibir_mensagem('ATÉ LOGO!')
