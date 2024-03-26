preço = float(input('preço das compras: '))
print('''FORMAS DE PAGAMENTO
      [1] à vista dinheiro/cheque
      [2] à vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão
       ''')
opção = int(input('qual é a opção? '))
if opção == 1:
    total = preço - (preço*0.10)
    print('o valor a ser pago caiu de {:.1f} para {:.2f} R$'.format(preço,total))
elif opção == 2:
    total = preço - (preço*0.05)
    print('o valor a ser pago caiu de {:.1f} para {:.2f} R$'.format(preço,total))
elif opção == 3:
    parcela = preço/2
    print('o valor a ser pago é {:.2f} R$ dividido em 2 parcelas de {:.2f} R$ '.format(preço,parcela))
elif opção == 4:
    quantidade = int(input('você que pagar em quantas vezes? '))
    total = preço*1.20
    parcela = total/quantidade
    print('o valor a ser pago aumentou de {:.1f} para {:.1f} devido aos juros, esse valor será dividido em {} parcelas no valor de {:.2f} R$'.format(preço,total,quantidade,parcela))
else:
    print('Opção invalida tente novamente')