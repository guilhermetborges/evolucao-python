import funcoes
from time import sleep
arq = 'cursoemvideo.txt'

if funcoes.arquivoExiste(arq):
    print('arquivo encontrado com sucesso')
else:
    print('arquivo não encontrado')
    funcoes.criarArquivo(arq)

while True:
    resposta = funcoes.menu(['ver pessoas cadastradas ', 'cadastrar pessoa',  'Sair do Sistema'])
    if resposta == 1:
        # print('opção 1')
        funcoes.lerArquivo(arq)
    elif resposta == 2:
        print('opção 2')
        funcoes.cabeçalho('NOVO CADASTRO')
        nome = str(input('nome: '))
        idade =  funcoes.leiaint('Idade: ')
        funcoes.cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
