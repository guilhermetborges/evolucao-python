try:
    a = int(input('digite um numero: ' ))
    b = int(input('digite outro nmr: '))
    r = a/b#except (ValueError,TypeError):
    print('OPA,tivemos um problema com os tipos de dados')
except KeyboardInterrupt:
    print('o usuario preferiu não informar os dados')
except Exception as erro:
    print(f'o erro encontrado foi {erro.__cause__}')
else:
    print(f'o resultado é {r}')
finally:
    print('obrigado, volte sempre!')