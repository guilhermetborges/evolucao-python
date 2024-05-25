def leiaint(msg):
    while True:
        try:
            entrada = int(input(msg))
        except(ValueError,TypeError):
            print('\033[0;31mERRO, FOI DIGITADO UM NUMERO INVALIDO!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO, ENTRADA DE DADOS INTERRONPIDA PELO USUARIO!\033[m')
            return 0
        else:
            return entrada
            

def linha(tam = 42):
    return('¬') * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaint('\033[32mSua Opção: \033[m')
    
    return opc

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('ouve um erro na criação do arquivo')
    else:
        print(f'arquivo {name} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos' )

        print(a.read())


def cadastrar(arq, nome='desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('ouve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')

